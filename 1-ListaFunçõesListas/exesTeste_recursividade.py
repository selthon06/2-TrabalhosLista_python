# ==========================================
# EXERCÍCIO 1 — PERCORRENDO UMA LISTA
# ==========================================

# Crie uma lista com 5 números e use um for
# para imprimir cada número.


# ==========================================
# EXERCÍCIO 2 — SEPARANDO PARES E ÍMPARES
# ==========================================

numeros = [3, 8, 11, 20, 25, 30, 42]

# Crie duas listas:
# pares = []
# impares = []

# Percorra a lista numeros e coloque cada
# número na lista correta.


# ==========================================
# EXERCÍCIO 3 — DOBRAR OS VALORES
# ==========================================

# Crie uma função chamada:
# dobrar_numeros(lista)

# Ela deve receber uma lista e retornar
# uma nova lista com todos os valores dobrados.

# Exemplo:
# numeros = [2, 4, 6, 8]
# Resultado esperado:
# [4, 8, 12, 16]

# Tente fazer de maneira que a lista original
# não seja alterada.


# ==========================================
# EXERCÍCIO 4 — MAIOR, MENOR E SOMA
# ==========================================

# Crie uma função chamada:
# analisar_numeros(lista)

# Ela deve receber uma lista e mostrar:
# - O maior número
# - O menor número
# - A quantidade de números
# - A soma dos números

# Exemplo:
# numeros = [10, 5, 30, 2, 15]

# Resultado esperado:
# Maior: 30
# Menor: 2
# Quantidade: 5
# Soma: 62

# Dica:
# Você pode usar max(), min(), len() e sum()


# ==========================================
# EXERCÍCIO 5 — CADASTRO DE NOMES
# ==========================================

# Crie uma função chamada:
# adicionar_nome(nome, lista=None)

# A função deve:
# 1. Verificar se lista é None.
# 2. Se for None, criar uma lista vazia.
# 3. Adicionar o nome na lista.
# 4. Retornar a lista.

# Teste:

# nomes = adicionar_nome("Ana")
# print(nomes)

# nomes = adicionar_nome("Carlos", nomes)
# print(nomes)

# nomes = adicionar_nome("João", nomes)
# print(nomes)

# Resultado esperado:
# ['Ana']
# ['Ana', 'Carlos']
# ['Ana', 'Carlos', 'João']