# ============================================================
# utils.py — A Caixa de Ferramentas
# Funções auxiliares reutilizáveis: formatação visual e
# validações. Princípio DRY: escreva uma vez, use em todo lugar.
# ============================================================


def linha():
    """Imprime uma linha separadora de '=' com 50 caracteres."""
    print("=" * 50)


def linha_simples():
    """Imprime uma linha separadora de '-' com 50 caracteres."""
    print("-" * 50)


def titulo(texto):
    """
    Exibe um título centralizado entre duas linhas separadoras.
    Parâmetro:
        texto (str): o título a ser exibido.
    """
    print()
    linha()
    print(texto.center(50))
    linha()


def subtitulo(texto):
    """
    Exibe um subtítulo com linha simples abaixo.
    Parâmetro:
        texto (str): o subtítulo a ser exibido.
    """
    print(f"\n  {texto}")
    linha_simples()


def exibir_cardapio(cardapio):
    """
    Exibe o cardápio completo organizado por categoria.
    Parâmetro:
        cardapio (list): lista de dicionários do cardápio (de dados.py).
    """
    titulo("CARDÁPIO DO RESTAURANTE")

    categorias = []
    for item in cardapio:
        if item["categoria"] not in categorias:
            categorias.append(item["categoria"])

    for cat in categorias:
        subtitulo(cat)
        for item in cardapio:
            if item["categoria"] == cat:
                print(f"  [{item['codigo']:02d}] {item['nome']:<30} R$ {item['preco']:.2f}")

    linha()


def validar_numero_inteiro(mensagem):
    """
    Solicita um número inteiro ao usuário com tratamento de erro (try/except).
    Continua pedindo até receber um valor válido.
    Parâmetro:
        mensagem (str): texto exibido no input.
    Retorno:
        int: o número inteiro informado pelo usuário.
    """
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("  ⚠  Digite um número inteiro válido.")


def validar_numero_float(mensagem):
    """
    Solicita um número decimal ao usuário com tratamento de erro (try/except).
    Parâmetro:
        mensagem (str): texto exibido no input.
    Retorno:
        float: o número decimal informado pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("  ⚠  Digite um valor numérico válido (ex: 2).")