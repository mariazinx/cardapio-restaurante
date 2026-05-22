# 🍽️ Gerenciador de Cardápio de Restaurante

**Tema:** Cardápio de Restaurante  
**Disciplina:** Programação de Computadores  
**Professora:** Profa. Dra. Andréa Ono Sakai  
**Período/Turma:** 2026.1
**Este trabalho foi feito por: Maria Eduarda Alves e Higor Aparecida
---

## 📋 Descrição do Projeto

Sistema de gerenciamento de pedidos de restaurante desenvolvido em Python, organizado em múltiplos arquivos. O sistema permite fazer pedidos a partir de um cardápio com preços, gerenciar a fila de preparo da cozinha, acompanhar o status de cada pedido, visualizar o histórico de entregas e calcular a conta por mesa.

---

## 📚 Explicação Conceitual

### Fila (FIFO — First In, First Out)

Uma fila funciona como a fila de espera de um restaurante: quem pediu primeiro é atendido primeiro. No Python, usamos uma lista comum com `.append()` para inserir no final e `.pop(0)` ou `.remove()` para retirar do início.

No projeto, a `fila_preparo` armazena os pedidos que aguardam preparo na cozinha. Quando um novo pedido é feito, ele entra no final da fila. O pedido mais antigo (índice 0) é o primeiro a ser preparado.

```python
# dados.py
fila_preparo = []   # fila FIFO dos pedidos aguardando preparo

# tarefas.py — ao cadastrar um pedido:
dados.fila_preparo.append(dict_pedido)   # entra no final (FIFO)

# ao cancelar ou entregar:
dados.fila_preparo.remove(pedido)        # sai pelo início ou por busca
```

---

### Pilha (LIFO — Last In, First Out)

Uma pilha funciona como uma pilha de pratos: o último colocado é o primeiro a ser retirado. No Python, usamos `.append()` para empilhar e `reversed()` para ler do topo para a base.

No projeto, a `pilha_entregues` guarda o histórico de pedidos entregues. O pedido mais recentemente entregue aparece primeiro na visualização do histórico.

```python
# dados.py
pilha_entregues = []   # pilha LIFO do histórico de entregas

# tarefas.py — ao marcar um pedido como "Entregue":
dados.pilha_entregues.append(pedido)   # empilha no topo

# ao exibir o histórico:
for i, pedido in enumerate(reversed(dados.pilha_entregues), start=1):
    print(pedido['item'])   # lê do topo para a base (LIFO)
```

---

### Dicionário

Cada pedido do sistema é armazenado como um dicionário Python — um conjunto de pares chave-valor. Isso permite agrupar todos os atributos de um pedido em uma única estrutura e acessar qualquer campo pelo nome, não pela posição.

```python
dict_pedido = {
    "id":         len(dados.pedidos) + 1,
    "mesa":       mesa,
    "item":       item_escolhido["nome"],
    "categoria":  item_escolhido["categoria"],
    "preco_unit": item_escolhido["preco"],
    "quantidade": quantidade,
    "total":      round(item_escolhido["preco"] * quantidade, 2),
    "prioridade": prioridade,
    "status":     dados.status[0]   # "Aguardando"
}
```

---

### Lista vs Tupla

**Lista** (`[]`): mutável e ordenada. Usada para armazenar coleções que mudam ao longo da execução — pedidos são adicionados e removidos o tempo todo.

```python
pedidos      = []   # todos os pedidos — cresce com .append(), diminui com .remove()
fila_preparo = []   # pedidos aguardando — entra e sai conforme o fluxo
```

**Tupla** (`()`): imutável e ordenada. Usada para valores fixos que não devem ser alterados durante a execução, como as categorias de status e os níveis de prioridade. Por serem imutáveis, protegem o sistema contra alterações acidentais.

```python
status      = ("Aguardando", "Em Preparo", "Entregue")   # imutável
prioridades = ("Normal", "Urgente", "VIP")               # imutável

# Acesso por índice — igual ao modelo da aula:
pedido["status"] = dados.status[0]   # "Aguardando"
pedido["status"] = dados.status[1]   # "Em Preparo"
pedido["status"] = dados.status[2]   # "Entregue"
```

---

### Modularização

O sistema é dividido em 4 arquivos `.py`, cada um com uma responsabilidade clara. Isso aplica o princípio **DRY (Don't Repeat Yourself)**: funções escritas uma vez e reutilizadas em qualquer lugar via `import`.

| Arquivo      | Responsabilidade                                                            |
| ------------ | --------------------------------------------------------------------------- |
| `dados.py`   | Variáveis globais: lista, fila, pilha, tuplas e cardápio fixo               |
| `utils.py`   | Funções auxiliares: formatação visual, validações com `try/except`          |
| `tarefas.py` | Regras de negócio: cadastrar, listar, atualizar, cancelar, histórico, conta |
| `main.py`    | Ponto de entrada: menu com `while True`, `if/elif` e `break` para sair      |

```python
# Exemplo de como main.py importa e usa os outros módulos:
from dados  import pedidos, fila_preparo
from utils  import titulo, linha
from tarefas import cadastrar_pedido, listar_pedidos
```

---

## ▶️ Como Executar o Projeto

**Requisitos:** Python 3.10 ou superior. Nenhuma biblioteca externa necessária.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gerenciador_cardapio.git

# Entre na pasta
cd gerenciador_cardapio

# Execute o programa
python main.py
```

---

## ✅ Funcionalidades Implementadas

### Obrigatórias

- [x] Cadastrar pedido (mesa, item do cardápio, quantidade, prioridade)
- [x] Listar todos os pedidos com status atual
- [x] Fila de preparo — FIFO: pedido mais antigo preparado primeiro
- [x] Pilha de pedidos entregues — LIFO: último entregue aparece primeiro
- [x] Atualizar status: Aguardando → Em Preparo → Entregue
- [x] Cancelar pedido com `.remove()` (verificação prévia para evitar erro)

### Bônus

- [x] Calcular total da conta por mesa
- [x] Cardápio fixo organizado por categoria (Prato Principal, Entrada, Sobremesa, Bebida) com 15 itens e preços

---

## 💬 Dificuldades e Aprendizados

A maior dificuldade foi entender como a mesma variável pode ser compartilhada entre os arquivos usando `import dados` e modificada através de `dados.pedidos.append()`, em vez de importar diretamente com `from dados import pedidos`. Quando importamos diretamente, criamos uma cópia local da referência, e mudanças feitas em um arquivo não refletem nos outros — isso causou bugs difíceis de rastrear no início.

Outro ponto desafiador foi a lógica de sincronizar a lista geral com a fila de preparo: um pedido precisa existir em ambas ao ser criado, e ser removido da fila ao ser entregue ou cancelado, sem ser removido da lista geral no caso de entrega. Entender quando usar `.remove()` versus simplesmente ignorar o item exigiu pensar no fluxo completo do sistema.

A implementação do LIFO com `reversed()` foi um momento de clareza: não precisamos inverter a lista ou usar estruturas complexas — basta ler de trás para frente na hora de exibir. Isso mostrou que a escolha certa de ferramenta do Python pode simplificar muito o código.

---

## 📁 Estrutura do Repositório

```
gerenciador_cardapio/
├── main.py       # ponto de entrada (menu)
├── dados.py      # variáveis globais (lista, fila, pilha, tuplas, cardápio)
├── tarefas.py    # regras de negócio (cadastrar, listar, atualizar...)
├── utils.py      # funções auxiliares (formatação, validações)
└── README.md
```
