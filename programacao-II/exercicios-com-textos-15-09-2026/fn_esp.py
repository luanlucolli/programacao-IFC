"""Crie um arquivo fn_esp.py com as seguintes funções:

1 - Recebe uma string e retorna a qtd de vogais

2 - Recebe uma string e Retorna a qtd de consoantes

3 - Recebe uma string e Retorna a qtd de números

4 -  Recebe uma string e Retorna a qtd de caracteries especiais (@#$%&_+=-?! etc.)

5 -  Recebe uma string e retorna um array com todos os índices das vogais,

6 -  Recebe uma string e retorna um array com todos os índices das consoantes.

7 -  Recebe uma string e retorna um array com todos os índices de todos os caracteres que são números.

8 - Recebe uma string e gera um array com os números dessa string. Após isso, a função deve imprimir elemento por elemento do array  informando cada um se é par ou ímpar.
Ex: se digitado pelo  usuário a string: "abc12345!?" deverá ser impresso na tela:
1 - impar
2 - par
3 - impar
4 - par
5 - impar

----------------------------------------------------------------------------------------------

Crie um outro arquivo chamado de main_principal.py. Nele,importe todas as funções do arquivo fn_esp.py com apelidos individuais. Solicite ao usuário que digite alguma frase e ao final exiba na tela as quantidades de vogais, consoantes, números e caracteres especiais. Exiba também os indices das vogais, consoantes, números e caracteres especiais, bem como a impressão dos números da mensagem se são pares ou ímpares.
"""


def countVogais(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador += 1

    return contador


def countConsoantes(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "bcdfghjklmnpqrstvwxyz":
            contador += 1

    return contador


def countNumeros(texto):
    contador = 0
    for letra in texto:
        if letra in "0123456789":
            contador += 1

    return contador


def countCaracterEspecial(texto):
    contador = 0
    for letra in texto:
        if letra in "@#$%&_+=-?!":
            contador += 1

    return contador


def indicesVogais(texto):
    indices = []
    for i in range(len(texto)):
        if texto[i].lower() in "aeiou":
            indices.append(i)
    return indices


def indicesConsoantes(texto):
    indices = []
    for i in range(len(texto)):
        if texto[i].lower() in "bcdfghjklmnpqrstvwxyz":
            indices.append(i)
    return indices


def indicesNumeros(texto):
    indices = []
    for i in range(len(texto)):
        if texto[i] in "0123456789":
            indices.append(i)
    return indices


def indicesCaracterEspecial(texto):
    indices = []
    for i in range(len(texto)):
        if texto[i] in "@#$%&_+=-?!":
            indices.append(i)
    return indices


def arrayIsPair(texto):
    numeros = []
    for letra in texto:
        if letra in "0123456789":
            numero = int(letra)
            numeros.append(numero)
            if numero % 2 == 0:
                print(numero, "- par")
            else:
                print(numero, "- ímpar")
