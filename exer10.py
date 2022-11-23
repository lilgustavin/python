num1 = input('informe o valor 1: ')
divisor = input('informe o valor div: ')

if num1.isalpha():
    print('nao é um numero')

if num1.isdecimal():
    print('é um numero')

if int (divisor) > 0:
    print('posso dividir')
    divisao = int(num1) / int(divisor)
print(f'resultado da divisao é {divisao}')
