print('Cálculo do IMC \n')

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
print('\n')

calculoIMC = peso / (altura**2)

if calculoIMC <= 18.5:
    print(' Seu IMC é %f' %calculoIMC, '\n Você está abaixo do peso ideal!')
elif calculoIMC >= 18.6 and calculoIMC <= 24.9:
    print(' Seu IMC é %f' %calculoIMC, '\n Você está no peso ideal!')
elif calculoIMC >= 25 and calculoIMC <= 29.9:
    print(' Seu IMC é %f' %calculoIMC , '\n Você está acima do peso!')
elif calculoIMC >= 30 and calculoIMC <= 34.9:
    print(' Seu IMC é %f' %calculoIMC , '\n Seu estado de obesidade é de Grau I!')
elif calculoIMC >=35 and calculoIMC <= 39.9:
    print(' Seu IMC é %f' %calculoIMC , '\n Seu estado de obesidade é de Grau II (severa)!!')
else:
    print(' Seu IMC é %f' %calculoIMC , '\n Seu estado de obesidade é de Grau III (mórbida)!!!')
