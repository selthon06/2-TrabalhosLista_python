# Lista de Exercícios - Listas 
# 1 - Média Móvel: Escreva uma função que receba uma lista de números e um número 
# inteiro k (tamanho da janela). A função deve retornar uma lista com as médias de cada 
# sublista contígua de tamanho k. 


# 2 - Deslocamento (Shift) à Direita: Crie uma função que receba uma lista e um inteiro n. 
# A função deve retornar uma nova lista com os elementos deslocados n posições para a 
# direita. Os elementos que "saírem" do final devem reaparecer no início. 


# 3 - Concatenação Alternada: Desenvolva uma função que receba duas listas (de 
# tamanhos possivelmente diferentes) e retorne uma única lista intercalando os elementos 
# de ambas até o fim da menor, adicionando o restante da maior ao final. 

# 4 - Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já 
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo 
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar 
# algoritmo de ordenação depois. 

lista1 = [10, 20, 30, 40, 50]
lista2 = [9, 19, 44, 49, 60]
def merge_listas(lista1, lista2):
    listageral = lista1 + lista2

    for merge in listageral:
        print(merge)
        sorted(listageral)

    return listageral

merge_listas(lista1, lista2)

# 5 - Controle de Qualidade Agrícola: Uma fazenda colhe maçãs e as classifica pelo peso 
# (em gramas). Você receberá a lista de pesos, o peso mínimo para exportação e o peso 
# máximo. 
# Retorno exigido: Uma lista contendo os pesos aprovados, uma segunda lista com 
# os pesos descartados, e a porcentagem de perda da safra (número float). 

# 6 - Sistema de Alerta de Manutenção de Frota: Um ônibus transmite diariamente a 
# quilometragem percorrida. Você receberá uma lista com esses trajetos diários e o limite 
# de quilometragem para a revisão do motor.
# Retorno exigido: A quilometragem total acumulada, o dia (índice da lista) em 
# que o limite foi ultrapassado, e um booleano (True ou False) indicando se o 
# ônibus precisa ser recolhido imediatamente. 

# 7 - Análise de Turbulência em Voo: Os sensores de um avião registram a altitude a cada 
# minuto (lista de números). Uma turbulência severa é caracterizada por uma queda de 
# altitude maior que 500 metros em um único minuto. 
# Retorno exigido: True ou False se houve turbulência severa, e a maior queda 
# registrada em um minuto durante todo o voo. 

# 8 - Apuração de Urna Eletrônica: Recebemos uma lista gigantesca embaralhada 
# contendo os IDs dos candidatos que receberam votos. O voto em branco é o ID 0. O 
# sistema não sabe previamente quais são os IDs válidos. 
# Retorno exigido: Uma estrutura em formato de lista de listas (ex: [[id, 
# total_votos], ...]) resumindo a eleição, o ID do candidato vencedor e a 
# porcentagem de votos em branco. 

# 9- Escala Crítica de Plantão Médico: Um hospital fornece uma lista onde cada elemento 
# é uma sublista com os dias do mês em que um médico específico pode trabalhar. O 
# diretor quer saber qual é o dia do mês que tem a menor cobertura de profissionais. 
# Retorno exigido: O dia (número) com a menor quantidade de médicos 
# disponíveis e uma lista com os índices (IDs) dos médicos que farão plantão 
# nesse dia crítico. 

# 10 - Decodificador de Sinais de Satélite: Um satélite envia pacotes de dados como uma 
# lista de bits (0s e 1s). Um pacote de informação válido é sempre sinalizado pelo padrão 
# exato de um 1 seguido imediatamente por dois 0s. 
# Retorno exigido: O número total de pacotes válidos detectados e uma lista de 
# índices marcando onde cada pacote válido começa.