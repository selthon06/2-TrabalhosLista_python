
# numbers = [2,4,6]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)



#bicycles = ['trek','cannondale','redline', 'specialized']

# for bicycle in bicycles:
#     print(bicycle)

#bicycles[-2] = 3 

#print(bicycles[-2]) #número negativo acessa os 
                        #últimos elementos da lista
#print(bicycles[0].title()) #formata com a inicial maiúscula
#print(bicycles[0])

#print(bicycles)
#bicycles.insert(1, 'teste') #insere na posição especificada
#print(bicycles)

#del bicycles[1] #remove da posição especificada
#print(bicycles)


#bicycles_popped = bicycles.pop() #remove do fim da lista

#print(bicycles)
#print(bicycles_popped)

# bicycles_popped = bicycles.pop(1) #remove da posição especificada
# print(bicycles)
# print(bicycles_popped)

# bicycles.remove('redline') #remove pelo elemento e não pela posição
# print(bicycles)

#numbers = [2,6,4]

# print(max(numbers)) #maior valor
# print(min(numbers)) #menor
# print(sum(numbers)) #soma todos os elementos
# print(len(numbers)) #retorna o tamanho da lista

# nomes = ['Ana', 'Ronaldo', 'Neymar']
# print(max(nomes))
# print(min(nomes))




# numeros = [2,5,6,9,10,1]
# pares = []
# impares = []
# qtd_pares = 0

# for item in numeros:
#     if item % 2 == 0:
#         pares.append(item)
#         qtd_pares += 1
#     else:
#         impares.append(item)

# print("Quantidade de números pares ", len(pares))
# print(pares)

# for i in pares:
#     print(i)

#for i in range(len(numeros)):





# #cars = ['bmw', 'Audi', 'toyota','Bmw', 'bamw', 'honda']
# cars = [50, 30, 40, 0,60]
# cars.sort() #ordena dentro da própria lista
# print(cars)





# cars = ['bmw', 'Audi', 'toyota', 'honda']
# cars = [50, 30, 40, 0,60]
# cars.sort(reverse=True) #ordena dentro da própria lista, mas em ordem decrescente
# print(cars)





# cars = ['bmw', 'Audi', 'toyota', 'honda']
# print(sorted(cars)) #ordena, mas não salva na própria lista
# print(cars) #mantém os dados na lista original





# cars = ['bmw', 'toyota', 'honda', 'audi']
# cars.reverse() #inverte os elementos da lista
# print(cars)


# teste = []
# if len(teste) > 0: #teste para não dar erro de indice na lista, 
#                     #tentar acessar indice que não existe
#     print(teste[0])



# lista = list(range(2,11,2)) #cria a lista com os valores do range = 
#                             #começando no 2, indo até o 11 e indo de 2 em 2
# print(lista)

# lista = [] #criar uma lista vazia
# for i in range(1,11):
#     item = i**2 #** exp.
#     lista.append(item)

# print(lista)    

# squares = [i**2 for i in range(1,11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players)
#print(players[0:3]) #inicia na posição 0 e retorna 3 elementos

#print(players[:4])

#print(players[2:])
#teste = players[-2:] 
#print(players[-2:])



# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for i in players[:3]:
#     print(i.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print("My favorite foods are:")
# print(friend_foods)



#Altera a lista original
# def processar_numeros(lista):
#     for i in range(len(lista)):
#         lista[i] *= 2  
#     return lista #retorna a lista modificada

# lista_original = [1, 2, 3, 4] #Lista original
# print(lista_original)
# resultado = processar_numeros(lista_original)

# print(resultado)     
# print(lista_original)  



#preserva a lista original
# def inverter_lista(lista):
#     lista.reverse()
#     return lista

# lista_original = [10, 20, 30]
# print(lista_original)
# resultado = inverter_lista(lista_original[:]) #passando uma cópia da lista

# print(resultado)  
# print(lista_original)    




# def adicionar_item_errado(item, lista=[]):
#     lista.append(item)
#     return lista

# print(adicionar_item_errado(1))  
# print(adicionar_item_errado(2))  




def adicionar_item_correto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(adicionar_item_correto(1))  
print(adicionar_item_correto(2))  
