peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura * altura)

if imc < 18.5:
    print('abaixo do peso')

else:
    if imc >= 18.6 and imc <= 24.9:
        print('saudavel')

    elif imc >= 25 and imc <= 29.9:
        print('peso em excesso')

    elif imc >= 30 and imc <= 34.9:
        print('obesidade I')

    elif imc >= 35 and imc <= 39.9:
        print('obesidade II')

    else:
        print('obesidade III')