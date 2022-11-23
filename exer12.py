from os import system
import random

system('cls')

#print(random.randint(0,100))

num = random.randint(0,100)

#o numero e par ou impar?

resto = num % 2
if resto == 0:
    print('o numero e par')
else:
    print('o numero e impar')

#o numero escolhido e maior que 50 ou menor
# (mais perto do 100 ou do 0)
if num > 50:
    print('o numero escolhido esta mais perto 100')
else:
    print('o numero escolhido esta mais perto do 0')

# o numero escolhido e primo
