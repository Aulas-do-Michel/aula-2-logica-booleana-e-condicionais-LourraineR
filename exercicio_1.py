"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""

numero_digitado = int(input('digite um número'))
if numero_digitado % 2 == 0:
    print('Seu número é par!')
    
else:
    print('Seu número é impar!')
