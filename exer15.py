# faça um programa que receba 3 numeros e informe
# qual numero e o maior e qual e o menor

num1 = (input('informe o primeiro valor: '))
num2 = (input('informe o seugundo valor: ')) 
num3 = (input('informe o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é maior e {num2} e {num3} sao menores')

elif num2 < num1 and num2 > num3:
   print(f'{num2} é o maior e {num1} e {num3}')

else:
   print(f'{num3} é o maior e {num1} e {num2}')
