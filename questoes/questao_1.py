## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario = float(input('Qual é o salario do funcionario?'))
    novo = salario + (salario * (30 / 100))
    print('O funcionário ganhava R${:.2f}, com 30% de aumento, passa a receber R${:.2f}'.format(salario, novo))
if __name__ == '__main__':
    main()
