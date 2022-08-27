#Premissas assumidas
Linguagem: Python 3.8.5
Sistema Operacional: Linux - Ubuntu
Ambiente de desenvolvimento: PyCharm

#Decisões de projeto
Criei uma função para cada situação dos Pets Shops, tendo como retorno o
somatório do preço dos serviços. Esse retorno foi alocado em uma lista, com três tuplas.
Dentro de cada tupla, foram incluídos 03 argumentos (retorno da função, distância, nome do
Pet Shop).

Para definir qual Pet Shop oferta o melhor valor, foi utilizado o método sorted() para
ordenação da lista, e o itemgetter do módulo operator para utilização de dois parâmetros na
ordenação. O itemgetter recebeu como parâmetros, o valor total dos serviços e a distância
do canil em relação ao Pet Shop, para que em caso de empate, ordenasse pelo Pet Shop
mais próximo.

Levando em consideração a quantidade pequena de valores a serem comparados,
poderia ter sido utilizado "if", mas preferi o método de ordenação por ser possível resolver o
problema com uma menor quantidade de código, facilitando assim a compreensão por
outros desenvolvedores.

#Instruções para executar o sistema
Conforme expressado anteriormente, utilizei a IDE PyCharm para implementação do
desafio proposto, dessa forma recomendo-a para executar o código enviado. Como
alternativa, sugiro acessar o diretório do projeto pelo terminal, seguido do comando python
principal.py.