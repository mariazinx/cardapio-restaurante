# ============================================================
# main.py — A Sala de Controle
# Ponto de entrada do programa. Contém o menu principal com
# loop while True e os desvios if/elif para cada funcionalidade.
# Execute: python main.py
# ============================================================

import dados
from utils import titulo, linha
from tarefas import (
    cadastrar_pedido,
    listar_pedidos,
    listar_fila_preparo,
    atualizar_status,
    cancelar_pedido,
    ver_historico_entregues,
    calcular_conta_mesa,
)


def mostrar_menu():
    """Exibe o menu principal do sistema."""
    titulo("GERENCIADOR DE CARDÁPIO — RESTAURANTE")
    print("  1. Fazer Pedido")
    print("  2. Listar Todos os Pedidos")
    print("  3. Ver Fila de Preparo (FIFO)")
    print("  4. Atualizar Status do Pedido")
    print("  5. Cancelar Pedido")
    print("  6. Ver Histórico de Entregues (LIFO)")
    print("  7. Calcular Conta da Mesa")
    print("  8. Sair")
    linha()


# ── Loop principal — roda até o usuário escolher "Sair" ──
while True:
    mostrar_menu()

    opcao = input("  Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_pedido()

    elif opcao == "2":
        listar_pedidos()

    elif opcao == "3":
        listar_fila_preparo()

    elif opcao == "4":
        atualizar_status()

    elif opcao == "5":
        cancelar_pedido()

    elif opcao == "6":
        ver_historico_entregues()

    elif opcao == "7":
        calcular_conta_mesa()

    elif opcao == "8":
        print()
        linha()
        print("  Encerrando o sistema. Até logo!")
        linha()
        break

    else:
        print("\n  ⚠  Opção inválida. Tente novamente.")

    input("\n  Pressione ENTER para continuar...")