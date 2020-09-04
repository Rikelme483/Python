print('Questionário One Piece.\n')
cont = int(0)
print('1. Como se chama o cientista mais famoso da marinha e responsável pelo projeto Pacifista? \n')
print(' a) Vegapunk \n b) Franky \n c) Caesar Clown \n')

resposta = input('Digite aqui sua resposta: ')

if resposta == 'a':
    print('Parabéns, você acertou! \n')
    cont = cont + 1
else:
    print('Você errou! \n')

print('Quantidade de Acertos: %d' % cont)

print('2. Como se chama o atual navio dos Mugiwara? \n')
print(' a) Merry \n b) Marineford \n c) Sunny')

resposta = input('Digite aqui sua resposta: ')

if resposta == 'c':
    print('Parabéns, você acertou! \n')
    cont = cont + 1
else:
    print('Você errou! \n')

print('Quantidade de Acertos: %d' % cont)


print('3. Qual Haki faz seu usuário nocautear seus oponentes sem nem mesmo tocá-los? \n')
print(' a) Haki do Armamento \n b) Haki do Julgamento \n c) Haki do Rei')

resposta = input('Digite aqui sua resposta: ')

if resposta == 'c':
    print('Parabéns, você acertou! \n')
    cont = cont + 1
else:
    print('Você errou! \n')

print('Quantidade de Acertos: %d' % cont)


print('4. Qual o nome da ilha em que vivem os samurais mais habilidosos do mundo? \n')
print(' a) Dressrosa \n b) Wano \n c) East Blue')

resposta = input('Digite aqui sua resposta: ')

if resposta == 'b':
    print('Parabéns, você acertou! \n')
    cont = cont + 1
else:
    print('Você errou! \n')

print('Quantidade de Acertos: %d' % cont)


print('5. Quantos Yonkous existem atualmente? \n')
print(' a) 4 \n b) 3 \n c) 2')

resposta = input('Digite aqui sua resposta: ')

if resposta == 'a':
    print('Parabéns, você acertou! \n')
    cont = cont + 1
else:
    print('Você errou! \n')

print('Quantidade de Acertos: %d \n' % cont)

if cont > 3:
    print('Parabéns, você é um fã de One Piece!!!')
else:
    print('Sinto muito, você não é um fã de One Piece, terá que ver o anime novamente :flushed:')