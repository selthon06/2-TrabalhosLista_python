

# tupla = ("r")

# print(type(tupla))

# tupla1 = ("r",)
# print(type(tupla1))

# t = tuple()
# print(t)
# print(type(t))

# t = tuple("selthon")
# print(t)

# numeros = [2, 4, 6, 8]

# print(numeros[0])
# print(numeros[1])

# numeros = (100, 50)
# print("valores originais")
# for numero in numeros:
#     print(numero)
# print("valores alterados")
# numeros = (300, 100)

# for numero in numeros:
#     print(numero)


# if (0, -1, -200000) < (0, 3, 4):
#     print("True")
# else:
#     print("False")

email = "selthon.leal@estudante.ifms.edu.br"
nomeusuario, dominio = email.split("@")
print(nomeusuario)
print(dominio)

txt = "algoritmos é a matéria mais facil do curso de ADS"
palavras = txt.split()
print(palavras)
lista= list()
for palavra in palavras:
    lista.append((len(palavra), palavra))
print(lista)

lista.sort(reverse=True)

res = list()
for tamanho, palavra in lista:
    res.append(palavra)
    print(tamanho)
    print(res)