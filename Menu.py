# Introdução de recebimentos dos dois valores inteiros
print('Bem vindo!\n')
num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

# Opção começa em 0
opcao = 0
while opcao != 7: # Mostra o menu para o usuário, tendo como opções os números de 1 a 7
    print('=-=' * 15)
    print('[ 1 ] Somar') # Realiza a soma dos valores inseridos
    print('[ 2 ] Subtrair') # Realiza a subtração dos valores inseridos
    print('[ 3 ] Multiplicar') # Realiza a multiplicação dos valores inseridos
    print('[ 4 ] Dividir') # Realiza a divisão dos valores inseridos
    print('[ 5 ] Maior') # Raliza a comparação dos valores e mostra qual o maior
    print('[ 6 ] Novos Números') # Da ao usuário a oportunidade de poder escolher novos valores
    print('[ 7 ] Sair do programa') # Sai do programa, encerrando o loop
    opcao = int(input('>>>>> Qual a opção que deseja? ')) # Usuário escolhe qual a opção desejada
    
    # Condições de acordo com as opções do usuário
    print('=-=' * 15)
    if opcao == 1: # Caso escolha opção 1
        soma = num1 + num2
        print(f'\nA soma dos números {num1} e {num2} é igual a {soma}\n')
    elif opcao == 2: # Caso escolha opção 2
        sub = num1 - num2
        print(f'\nA subtração de {num1} menos {num2} é igual a {sub}\n')
    elif opcao == 3: # Caso escolha opção 3
        mult = num1 * num2
        print(f'\nA Multiplicação de {num1} e {num2} é igual a {mult}\n')
    elif opcao == 4: # Caso escolha opção 4
        div = num1 / num2
        print(f'\nA Divisão de {num1} dividido por {num2} é igual a {div}\n')
    elif opcao == 5: # Caso escolha opção 5
        if num1 > num2: 
            print(f'\nEntre {num1} e {num2}, {num1} é maior!\n')
        else:
            print(f'\nEntre {num1} e {num2}, {num2} é maior!\n')
    elif opcao == 6: # Caso escolha opção 6
        num1 = int(input('\nInsira o primeiro valor novamente: \n'))
        num2 = int(input('\nInsira o segundo valor novamente: \n'))
    else: # Caso o usuário insira um valor diferente dos das opções, dara a seguinte mensagem de erro
        print('\nOpção inválida! por favor, tente novamente.\n')
# Caso o usuário escolha o número 7 (Sair do programa), o loop é encerrado e mostrará a mensagem final
print('\nVolte sempre!\n')