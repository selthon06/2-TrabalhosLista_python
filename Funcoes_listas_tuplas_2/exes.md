Lista de Exercícios – Listas
OBS: Todos os exercícios exigem a utilização de funções.

1 - Uma estufa inteligente possui vários sensores. O microcontrolador envia uma lista
de tuplas no formato (id_sensor, temperatura, umidade). As regras de segurança dizem
que a temperatura não pode passar de 35°C e a umidade não pode ficar abaixo de 20%.
Você precisa rastrear simultaneamente o maior valor de uma variável e o menor de
outra, enquanto filtra dados.
Retorno Exigido: Uma lista contendo apenas os id_sensor que dispararam algum
alarme de perigo, e uma tupla (maior_temperatura, menor_umidade) registrada em todo
o período.
Na Main: Crie uma lista simulando pelo menos 4 sensores (certifique-se de forçar pelo
menos um alerta de temperatura e um de umidade). Chame a função passando essa lista.
Imprima no terminal quais sensores entraram em alerta e exiba os picos máximos e
mínimos.

2 - Um serviço de streaming tem seu catálogo representado por uma lista de tuplas
(titulo_filme, ano_lancamento, genero, avaliacao_usuarios). Você também receberá
como parâmetro um genero_alvo (string) e uma nota_corte (float).
Você deve extrair dados com base em múltiplos parâmetros de entrada e encontrar o
"menor valor" (mais antigo) dentro de um subconjunto específico.
Retorno Exigido: Uma lista apenas com os títulos dos filmes que batem com o gênero
alvo e possuem nota igual ou superior ao corte, e uma tupla com o (titulo_filme,
ano_lancamento) do filme mais antigo dessa lista filtrada.
Na Main: Construa uma lista estática com pelo menos 4 filmes misturando gêneros e
notas. Defina variáveis para o seu gênero alvo e sua nota de corte. Invoque a função e
imprima a lista final de filmes aprovados, seguida de uma mensagem informando qual é
o filme mais antigo dentre os que foram filtrados.

3 - O sistema do caixa gera um recibo na forma de uma lista de tuplas (codigo_produto,
quantidade, preco_unitario).
Você deve multiplicar valores internos da tupla para criar dados novos (valor total do
item), acumular um montante geral e guardar o registro do maior valor calculado.
Retorno Exigido: O valor total da compra e uma tupla (codigo_produto,
valor_total_do_item) representando exclusivamente o item que teve o maior custo
absoluto na nota fiscal.
Na Main: Monte uma lista de tuplas representando o "carrinho" de um cliente com 3 ou
mais itens diferentes. Execute a função recebendo os retornos e imprima no terminal o
valor total da nota fiscal (formatado com R$ e duas casas decimais) e os detalhes do
produto que saiu mais caro na conta final.

4 - Em um motor gráfico, os obstáculos circulares são uma lista de tuplas (pos_x, pos_y,
raio). Você recebe também a tupla do jogador (jog_x, jog_y, jog_raio).
A colisão ocorre se a distância entre os centros (use a soma das diferenças absolutas de
X e Y como simplificação) for menor que a soma dos raios.
Retorno Exigido: Um booleano True ou False indicando se o jogador colidiu com
algum obstáculo e a quantidade exata de obstáculos com os quais ele está colidindo
simultaneamente.
Na Main: Defina uma lista com vários obstáculos espalhados pelo mapa e uma variável
separada para as coordenadas do jogador, forçando uma posição onde ele encoste em
pelo menos dois obstáculos ao mesmo tempo. Chame a função e exiba uma mensagem
de status ("Impacto Detectado!" ou "Caminho Livre") e a quantidade de objetos
atingidos.

5 - Uma imagem digital é formada por pixels. Você receberá uma lista de tuplas, onde
cada tupla contém três inteiros (R, G, B) representando as cores Vermelho, Verde e
Azul de um pixel (valores de 0 a 255).
Transforme o formato original dos dados convertendo uma tupla de três elementos em
um único valor inteiro (a média, usando divisão inteira), além de identificar uma
condição específica absoluta.
Crie uma nova lista contendo a média inteira de cada tupla e um contador informando
quantos pixels da imagem original eram puramente pretos (0, 0, 0).
Na Main: Crie uma lista simulando os pixels de uma foto pequena, garantindo que
contenha pelo menos um ou dois pixels totalmente pretos e outros variados. Passe essa
lista para a função e imprima a nova "imagem" processada, além do relatório
informando a quantidade exata de pixels escuros puros encontrados.