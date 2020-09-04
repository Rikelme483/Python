nome = input('Se apresente com seu nome: \n ')
print('Olá %s. Um prazer conhecê-lo. \n' % nome)

idade = input('Digite sua idade: \n')
print('Então você tem %s anos, que legal! \n' % idade)

hobby = input('O que você mais gosta de fazer? \n')
print('Que legal! %s parece ser muito divertido! \n' % hobby)

print('Vamos fazer um calculo ? \n')

num1 = input('Digite o primeito número: ')
num2 = input('Digite o segundo número: ')

print('\n')
print('Escolha um número operador. \n 1: adição \n 2: subtração \n 3: multiplicação \n 4: divisão \n')

calculo = input('Digite aqui: ')

if int(calculo) == 1:
    soma = float(num1) + float(num2)
    print('O resultado da Soma é: %d' % soma)
elif int(calculo) == 2:
    subt = float(num1) - float(num2)
    print('O resultado da Subtração é %d' % subt)
elif int(calculo) == 3:
    mult = float(num1) * float(num2)
    print('O resultado da Multiplicação é %d' % mult)
elif int(calculo) == 4:
    if float(num2) == 0:
        print('Não existe divisor por 0!!!')
    else:
        div = float(num1) / float(num2)
        print('O resultado da Subtração é %d' % div)




