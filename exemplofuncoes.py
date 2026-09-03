def estatisticas_basicas(valores):
    menor = min(valores)
    maior = max(valores)
    return menor, maior 

minimo, maximo = estatisticas_basicas([4, 1, 7, 20])
print(f'o minimo é: {minimo}, O maximo é: {maximo}')