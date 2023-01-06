altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: '))

imc = peso / (altura**2)
print(imc)

if imc < 18.5:
    print('Peso muito baixo')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc > 25 and imc <= 29.9:
    print('SOBREPESO')
elif imc > 30.0 and imc <= 39.9:
    print("OBESIDADE")
elif imc > 40.0:
    print("OBESIDADE GRAVE")
else:
    print ('Calculo não deifinido')