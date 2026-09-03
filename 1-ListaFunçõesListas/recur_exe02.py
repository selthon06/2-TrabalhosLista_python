# ==========================================
# EXERCÍCIO 2 — SEPARANDO PARES E ÍMPARES
# ==========================================

numeros = [3, 8, 11, 20, 25, 30, 42]

# Crie duas listas:
# pares = []
# impares = []

# Percorra a lista numeros e coloque cada
# número na lista correta.


for p in numeros:
    if p % 2==0:
        print(f'pares:', p)
print()
for i in numeros:
    if i % 2==1:
        print(f'impar:', i)