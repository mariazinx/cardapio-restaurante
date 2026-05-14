from dados import pedidos
from dados import fila_preparo
from dados import pilha_entregues

from utils import titulo


def cadastrar_pedido():

    titulo("CADASTRAR PEDIDO")

    mesa = input("Mesa: ")
    item = input("Item: ")
    quantidade = int(input("Quantidade: "))

    prioridades = ("Baixa", "Média", "Alta")

    print("\n1 - Baixa")
    print("2 - Média")
    print("3 - Alta")

    opcao = int(input("Escolha a prioridade: "))

    prioridade = prioridades[opcao - 1]

    pedido = {
        "id": len(pedidos) + 1,
        "mesa": mesa,
        "item": item,
        "quantidade": quantidade,
        "prioridade": prioridade,
        "status": "Aguardando"
    }

    pedidos.append(pedido)

    # FIFO
    fila_preparo.append(pedido)

    print("\nPedido cadastrado com sucesso!")


def listar_pedidos():

    titulo("PEDIDOS EM ABERTO")

    mesa = input("Digite a mesa: ")

    encontrou = False

    for pedido in pedidos:

        if pedido["mesa"] == mesa and pedido["status"] != "Entregue":

            encontrou = True

            print(f"""
ID: {pedido['id']}
Item: {pedido['item']}
Quantidade: {pedido['quantidade']}
Prioridade: {pedido['prioridade']}
Status: {pedido['status']}
""")

    if not encontrou:
        print("Nenhum pedido encontrado.")


def listar_todos():

    titulo("TODOS OS PEDIDOS")

    for pedido in pedidos:

        print(f"""
ID: {pedido['id']}
Mesa: {pedido['mesa']}
Item: {pedido['item']}
Quantidade: {pedido['quantidade']}
Prioridade: {pedido['prioridade']}
Status: {pedido['status']}
""")


def atualizar_status():

    titulo("ATUALIZAR STATUS")

    listar_todos()

    try:

        id_pedido = int(input("\nDigite o ID do pedido: "))

        for pedido in pedidos:

            if pedido["id"] == id_pedido:

                if pedido["status"] == "Aguardando":

                    pedido["status"] = "Em Preparo"

                elif pedido["status"] == "Em Preparo":

                    pedido["status"] = "Entregue"

                    # Remove da fila
                    if pedido in fila_preparo:
                        fila_preparo.remove(pedido)

                    # Adiciona na pilha
                    pilha_entregues.append(pedido)

                print("Status atualizado!")
                return

        print("Pedido não encontrado.")

    except:
        print("Digite um número válido.")


def cancelar_pedido():

    titulo("CANCELAR PEDIDO")

    listar_todos()

    try:

        id_pedido = int(input("\nDigite o ID do pedido: "))

        for pedido in pedidos:

            if pedido["id"] == id_pedido:

                if pedido in fila_preparo:
                    fila_preparo.remove(pedido)

                pedidos.remove(pedido)

                print("Pedido cancelado!")
                return

        print("Pedido não encontrado.")

    except:
        print("Digite um número válido.")


def ver_fila():

    titulo("FILA DE PREPARO")

    if len(fila_preparo) == 0:

        print("Fila vazia.")

    else:

        for pedido in fila_preparo:

            print(f"""
Mesa: {pedido['mesa']}
Item: {pedido['item']}
Status: {pedido['status']}
""")


def ver_entregues():

    titulo("PEDIDOS ENTREGUES")

    if len(pilha_entregues) == 0:

        print("Nenhum pedido entregue.")

    else:

        for pedido in reversed(pilha_entregues):

            print(f"""
Mesa: {pedido['mesa']}
Item: {pedido['item']}
Quantidade: {pedido['quantidade']}
""")


# FUNCIONALIDADE BÔNUS
def total_mesa():

    titulo("TOTAL DA MESA")

    mesa = input("Digite a mesa: ")

    total = 0

    for pedido in pedidos:

        if pedido["mesa"] == mesa:

            total += pedido["quantidade"] * 10

    print(f"Total da mesa: R$ {total}")


# FUNCIONALIDADE BÔNUS
def itens_mais_pedidos():

    titulo("ITENS MAIS PEDIDOS")

    contador = {}

    for pedido in pedidos:

        item = pedido["item"]

        if item in contador:

            contador[item] += pedido["quantidade"]

        else:

            contador[item] = pedido["quantidade"]

    for item, quantidade in contador.items():

        print(f"{item}: {quantidade}")