import math

print('Raiz quadrada de 34: ', math.sqrt(34))
print('cosseno de 21 graus: ', math.cos(21))
print('seno de 180 graus: ', math.sin(180))
print('tangente de 76 graus', math.tan(76), '\n')

import random

print('random.randrange de 100: ', random.randrange(100))
print('random.randrange de 50 á 100: ', random.randrange(50, 100))
print('random.choice de (20,5,10,15,54): ', random.choice([20, 5, 10, 15, 54]))
print('random.random: ', random.random())
print('random.randint de (30,60): ', random.randint(30, 60),'\n')

a = 15
b = 24
c = 24
print('a == b: ', a == b)
print('a != b: ', a != b)
print('a > b: ', a > b)
print('a < b: ', a < b)
print('a >= b: ', a >= b)
print('a <= b: ', a <= b, '\n')

print('A == B an B > c: ', a == b and b > c)
print('A != B or B < C: ', a != b or b < c)
print('not(A > B): ', not(a > b))
print('A > B and A < C: ', a > b and b < c)
print('A >= B or B == C: ', a >= b or b == c)
print('not(A <= B): ', not(a <= b))