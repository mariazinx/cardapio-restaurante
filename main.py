from utils import titulo

from pedidos import cadastrar_pedido
from pedidos import listar_pedidos
from pedidos import atualizar_status
from pedidos import cancelar_pedido
from pedidos import ver_fila
from pedidos import ver_entregues
from pedidos import total_mesa
from pedidos import itens_mais_pedidos


def mostrar_menu():

    titulo("RESTAURANTE")

    print("""
1 - Cadastrar pedido
2 - Listar pedidos por mesa
3 - Atualizar status
4 - Cancelar pedido
5 - Ver fila de preparo
6 - Ver pedidos entregues
7 - Total da mesa
8 - Itens mais pedidos
0 - Sair
""")


opcao = -1

while opcao != 0:

    mostrar_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        cadastrar_pedido()

    elif opcao == 2:

        listar_pedidos()

    elif opcao == 3:

        atualizar_status()

    elif opcao == 4:

        cancelar_pedido()

    elif opcao == 5:

        ver_fila()

    elif opcao == 6:

        ver_entregues()

    elif opcao == 7:

        total_mesa()

    elif opcao == 8:

        itens_mais_pedidos()

    elif opcao == 0:

        print("Programa encerrado.")

    else:

        print("Opção inválida.")