## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import *
def main ():
    raio = float(input("digite o valor do raio: "))
    area = pi * raio**2
    print(area)
    diametro = raio * 2
    print(diametro)
    comprimento = 2 * pi * raio
    print(comprimento)
if __name__ == '__main__':
    main()
