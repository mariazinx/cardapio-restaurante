# ============================================================
# dados.py — O Armazém de Dados
# Contém todas as variáveis globais do sistema:
# lista principal, fila (FIFO), pilha (LIFO) e tuplas fixas.
# ============================================================

# Lista principal: armazena todos os pedidos cadastrados
pedidos = []

# Fila (FIFO): armazena os pedidos aguardando preparo
# Novos pedidos entram no final (.append()) e saem pelo início (.pop(0))
fila_preparo = []

# Pilha (LIFO): armazena o histórico de pedidos entregues
# Último entregue aparece primeiro (lido com reversed())
pilha_entregues = []

# Tupla: status disponíveis — imutável, protege contra alterações acidentais
status = ("Aguardando", "Em Preparo", "Entregue")

# Tupla: prioridades disponíveis — imutável
prioridades = ("Normal", "Urgente", "VIP")

# Cardápio fixo do restaurante com preços
# Cada item é um dicionário com nome e preço
cardapio = [
    {"codigo": 1,  "nome": "Frango Grelhado",         "preco": 32.90, "categoria": "Prato Principal"},
    {"codigo": 2,  "nome": "Filé ao Molho Madeira",   "preco": 54.90, "categoria": "Prato Principal"},
    {"codigo": 3,  "nome": "Macarrão à Bolonhesa",    "preco": 28.50, "categoria": "Prato Principal"},
    {"codigo": 4,  "nome": "Salmão Grelhado",         "preco": 62.00, "categoria": "Prato Principal"},
    {"codigo": 5,  "nome": "Risoto de Cogumelos",     "preco": 38.90, "categoria": "Prato Principal"},
    {"codigo": 6,  "nome": "Salada Caesar",           "preco": 22.00, "categoria": "Entrada"},
    {"codigo": 7,  "nome": "Caldo de Feijão",         "preco": 14.50, "categoria": "Entrada"},
    {"codigo": 8,  "nome": "Pão de Alho (4 unid.)",   "preco": 12.00, "categoria": "Entrada"},
    {"codigo": 9,  "nome": "Pudim de Leite",          "preco": 16.00, "categoria": "Sobremesa"},
    {"codigo": 10, "nome": "Petit Gâteau",            "preco": 24.00, "categoria": "Sobremesa"},
    {"codigo": 11, "nome": "Sorvete (2 bolas)",       "preco": 14.00, "categoria": "Sobremesa"},
    {"codigo": 12, "nome": "Suco Natural (500ml)",    "preco": 11.00, "categoria": "Bebida"},
    {"codigo": 13, "nome": "Refrigerante Lata",       "preco":  7.50, "categoria": "Bebida"},
    {"codigo": 14, "nome": "Água Mineral",            "preco":  5.00, "categoria": "Bebida"},
    {"codigo": 15, "nome": "Café Expresso",           "preco":  6.00, "categoria": "Bebida"},
]