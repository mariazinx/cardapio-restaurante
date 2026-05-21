# ============================================================
# tarefas.py — O Motor de Regras
# Contém todas as funções de negócio do sistema:
# cadastrar pedido, listar pedidos, atualizar status,
# cancelar pedido, ver histórico e calcular conta da mesa.
# ============================================================

import dados
from utils import titulo, subtitulo, linha, linha_simples, exibir_cardapio, validar_numero_inteiro


def cadastrar_pedido():
    """
    Cadastra um novo pedido no sistema.
    - Exibe o cardápio para o usuário escolher o item pelo código.
    - Solicita mesa, quantidade e prioridade.
    - Cria um dicionário com todos os atributos do pedido.
    - Insere o pedido na lista global (tarefas.append) — registro geral.
    - Insere o pedido na fila de preparo (FIFO) — aguardando preparo.
    """
    exibir_cardapio(dados.cardapio)

    # Selecionar item do cardápio
    codigo_item = validar_numero_inteiro("  Digite o código do item: ")

    item_escolhido = None
    for item in dados.cardapio:
        if item["codigo"] == codigo_item:
            item_escolhido = item
            break

    if item_escolhido is None:
        print("  ⚠  Código inválido. Pedido não cadastrado.")
        return

    # Dados da mesa e quantidade
    mesa = validar_numero_inteiro("  Número da mesa: ")
    quantidade = validar_numero_inteiro("  Quantidade: ")
    if quantidade <= 0:
        print("  ⚠  Quantidade deve ser maior que zero.")
        return

    # Selecionar prioridade com base na tupla prioridades
    print()
    print("  Prioridades disponíveis:")
    for i, p in enumerate(dados.prioridades, start=1):
        print(f"    {i} - {p}")

    opcao_prioridade = validar_numero_inteiro("  Escolha a prioridade: ")

    if opcao_prioridade == 1:
        prioridade = dados.prioridades[0]   # "Normal"
    elif opcao_prioridade == 2:
        prioridade = dados.prioridades[1]   # "Urgente"
    elif opcao_prioridade == 3:
        prioridade = dados.prioridades[2]   # "VIP"
    else:
        prioridade = dados.prioridades[0]   # padrão: Normal

    # Montar o dicionário do pedido com todos os atributos
    dict_pedido = {
        "id":         len(dados.pedidos) + 1,
        "mesa":       mesa,
        "item":       item_escolhido["nome"],
        "categoria":  item_escolhido["categoria"],
        "preco_unit": item_escolhido["preco"],
        "quantidade": quantidade,
        "total":      round(item_escolhido["preco"] * quantidade, 2),
        "prioridade": prioridade,
        "status":     dados.status[0]   # "Aguardando" — status inicial via tupla
    }

    # Insere na lista principal (registro geral de todos os pedidos)
    dados.pedidos.append(dict_pedido)

    # Insere na fila de preparo (FIFO): entra no final, sai pelo início
    dados.fila_preparo.append(dict_pedido)

    print()
    linha()
    print(f"  ✔  Pedido #{dict_pedido['id']} cadastrado com sucesso!")
    print(f"     Mesa {mesa} | {quantidade}x {item_escolhido['nome']}")
    print(f"     Total: R$ {dict_pedido['total']:.2f} | Prioridade: {prioridade}")
    linha()


def listar_pedidos():
    """
    Lista todos os pedidos cadastrados no sistema.
    Usa enumerate para numerar os pedidos automaticamente.
    Exibe todos os atributos do dicionário de cada pedido.
    """
    titulo("TODOS OS PEDIDOS")

    if len(dados.pedidos) == 0:
        print("  Nenhum pedido cadastrado.")
        return

    for i, pedido in enumerate(dados.pedidos, start=1):
        print(f"  PEDIDO: {i}")
        print(f"  ID:          {pedido['id']}")
        print(f"  Mesa:        {pedido['mesa']}")
        print(f"  Item:        {pedido['item']}  ({pedido['categoria']})")
        print(f"  Quantidade:  {pedido['quantidade']}")
        print(f"  Preço Unit.: R$ {pedido['preco_unit']:.2f}")
        print(f"  Total:       R$ {pedido['total']:.2f}")
        print(f"  Prioridade:  {pedido['prioridade']}")
        print(f"  Status:      {pedido['status']}")
        linha_simples()


def listar_fila_preparo():
    """
    Exibe os pedidos que estão na fila de preparo (FIFO).
    O pedido mais antigo (índice 0) é o primeiro a ser preparado.
    """
    titulo("FILA DE PREPARO (FIFO)")

    if len(dados.fila_preparo) == 0:
        print("  Nenhum pedido na fila de preparo.")
        return

    print("  Ordem de preparo (mais antigo → mais recente):\n")
    for i, pedido in enumerate(dados.fila_preparo, start=1):
        print(f"  {i}º na fila | Mesa {pedido['mesa']} | {pedido['quantidade']}x {pedido['item']}"
              f" | Prioridade: {pedido['prioridade']}")
    linha()


def atualizar_status():
    """
    Atualiza o status de um pedido existente.
    Fluxo: Aguardando → Em Preparo → Entregue.
    - Se marcado como 'Entregue': adiciona à pilha de histórico (LIFO)
      e remove da fila de preparo.
    - Usa try/except para validar o ID digitado pelo usuário.
    """
    titulo("ATUALIZAR STATUS DO PEDIDO")

    listar_pedidos()

    if len(dados.pedidos) == 0:
        return

    # Validação com try/except: evita crash se usuário digitar texto
    try:
        id_pedido = int(input("  Digite o ID do pedido: "))
    except ValueError:
        print("  ⚠  Digite um número válido.")
        return

    for pedido in dados.pedidos:
        if pedido["id"] == id_pedido:

            print(f"\n  Status atual: {pedido['status']}")
            print("  Escolha o novo status:")
            for i, s in enumerate(dados.status, start=1):
                print(f"    {i} - {s}")

            opcao = validar_numero_inteiro("  Opção: ")

            if opcao == 1:
                pedido["status"] = dados.status[0]   # "Aguardando"
                # Se não estiver na fila, reinsere
                if pedido not in dados.fila_preparo:
                    dados.fila_preparo.append(pedido)

            elif opcao == 2:
                pedido["status"] = dados.status[1]   # "Em Preparo"

            elif opcao == 3:
                pedido["status"] = dados.status[2]   # "Entregue"
                # Empilha na pilha de histórico (LIFO): append() coloca no topo
                dados.pilha_entregues.append(pedido)
                # Remove da fila de preparo se ainda estiver lá
                if pedido in dados.fila_preparo:
                    dados.fila_preparo.remove(pedido)

            else:
                print("  ⚠  Opção inválida.")
                return

            print(f"\n  ✔  Status do pedido #{id_pedido} atualizado para '{pedido['status']}'.")
            return

    print("  ⚠  Pedido não encontrado.")


def cancelar_pedido():
    """
    Cancela um pedido removendo-o da fila de preparo com .remove().
    Só é possível cancelar pedidos que ainda estão na fila (Aguardando/Em Preparo).
    Verifica antes se o pedido está na fila para evitar erro.
    """
    titulo("CANCELAR PEDIDO")

    listar_fila_preparo()

    if len(dados.fila_preparo) == 0:
        return

    try:
        id_pedido = int(input("  Digite o ID do pedido para cancelar: "))
    except ValueError:
        print("  ⚠  Digite um número válido.")
        return

    for pedido in dados.pedidos:
        if pedido["id"] == id_pedido:
            # Verifica se o pedido ainda está na fila antes de remover
            if pedido in dados.fila_preparo:
                dados.fila_preparo.remove(pedido)   # remove da fila (FIFO)
                dados.pedidos.remove(pedido)        # remove da lista geral
                print(f"\n  ✔  Pedido #{id_pedido} cancelado e removido da fila.")
            else:
                print(f"  ⚠  Pedido #{id_pedido} já foi entregue e não pode ser cancelado.")
            return

    print("  ⚠  Pedido não encontrado.")


def ver_historico_entregues():
    """
    Exibe o histórico de pedidos entregues usando a pilha (LIFO).
    Usa reversed() para mostrar do mais recente para o mais antigo.
    O último entregue aparece primeiro — comportamento LIFO.
    """
    titulo("HISTÓRICO DE PEDIDOS ENTREGUES (LIFO)")

    if len(dados.pilha_entregues) == 0:
        print("  Nenhum pedido entregue ainda.")
        return

    # reversed() lê a pilha de cima para baixo (LIFO)
    for i, pedido in enumerate(reversed(dados.pilha_entregues), start=1):
        print(f"  ENTREGUE #{i}")
        print(f"  Mesa: {pedido['mesa']} | {pedido['quantidade']}x {pedido['item']}")
        print(f"  Total: R$ {pedido['total']:.2f} | Prioridade: {pedido['prioridade']}")
        linha_simples()


def calcular_conta_mesa():
    """
    Calcula e exibe o total da conta de uma mesa específica.
    Soma todos os pedidos daquela mesa (entregues ou não).
    Funcionalidade bônus do tema Cardápio de Restaurante.
    """
    titulo("CALCULAR CONTA DA MESA")

    if len(dados.pedidos) == 0:
        print("  Nenhum pedido cadastrado.")
        return

    mesa = validar_numero_inteiro("  Número da mesa: ")

    pedidos_mesa = [p for p in dados.pedidos if p["mesa"] == mesa]

    if len(pedidos_mesa) == 0:
        print(f"  ⚠  Nenhum pedido encontrado para a mesa {mesa}.")
        return

    print(f"\n  Pedidos da Mesa {mesa}:")
    linha_simples()
    total_geral = 0

    for pedido in pedidos_mesa:
        print(f"  {pedido['quantidade']}x {pedido['item']:<28} R$ {pedido['total']:>7.2f}  [{pedido['status']}]")
        total_geral += pedido["total"]

    linha()
    print(f"  TOTAL DA MESA {mesa}:              R$ {total_geral:>7.2f}")
    linha()