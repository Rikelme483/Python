
print('Calculo de Bhaskara \n')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2) - 4 * a * c
print('O valor de delta é: %f \n' % delta)

import math

raizDelta = float(math.sqrt(delta))
print('A raiz de delta vale: %f \n' % raizDelta)

x1 = ((-b) + raizDelta) / (2*a)
print('O valor de x1 é: %f' % x1)

x2 = ((-b) - raizDelta) / (2*a)
print('O valor de x2 é: %f' % x2)

