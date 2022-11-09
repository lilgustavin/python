#vamos trabalhar com dados de texto,
#usando varios metodos para verificar
#e modificar o valor de uma variavel da clss str

from os import system
system('cls')
nomeCompleto = input('Informe seu nome completo: ')
print(nomeCompleto)

#tamanho da string | total de caracteres
print ('1. total de caracteres :' , len(nomeCompleto))

#acessando um caracter a partir da posiçao
print('2. o caracter da posiçao 2 é: ',nomeCompleto[2])

#transformando um string em maiuscula | minuscula
print('3. texto em maiusculo' , nomeCompleto.upper())
print('4. texto em minusculo' , nomeCompleto.lower())
print('5. primeira letra maisculo' , nomeCompleto.capitalize())

#procurar a posiçao de um determinado caractere
print('6.na posiçao do caractere espaço: ' , nomeCompleto.find(' '))

#fatiar um string ate uma determinada posiçao
espaço = nomeCompleto.find (' ')
print('7. somente o nome: ' , nomeCompleto[0:espaço])

#substituir um caractere por outro
print('8. nome sem espaço: ' , nomeCompleto.replace(' ',''))

#verificar somente letras ou letras e numeros
print('9. tem somente letras? ' , nomeCompleto.replace(' ', '').isalpha())
print('10. É alfanumerico? ', nomeCompleto.replace(' ', '').isalnum())

#quebrar o texto em partes especificas retornando array
print('11. quebrar o texto a cada espaço em branco: ' , nomeCompleto.split(' '))

#centralizar texto usando * para completar as laterais
print ('12. centrakizar texto entre *' , nomeCompleto.center(80, '*'))