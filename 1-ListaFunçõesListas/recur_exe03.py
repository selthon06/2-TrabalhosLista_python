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
numeros = [2, 4, 6, 8]

def dobrar_numeros(lista):
    for lista in numeros:
        lista = numeros * 2
    return lista

