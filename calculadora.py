n1 = n2 = n3 = n4 = 0.0
media = 0.0

n1 = float(input('Digite a nota da primeira avaliação:'))
n2 = float(input('Digite a nota da segunda avaliação:'))
n3 = float(input('Digite a nota da terceira avaliação:'))
n4 = float(input('Digite a nota da quarta avaliação:'))

# Calcular a média

media = (n1 * 1.5 + n2 * 1.5 + n3 * 4.0 + n4 * 3.0) / 10

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print("Você está de recuperação!")
else:
    print("Aluno reprovado!")    

print('Sua média é {}'.format(media))