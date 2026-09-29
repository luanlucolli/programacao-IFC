"""Crie um programa em Python que tenha funções para cada um dos itens abaixo. Depois, execute cada uma."""

from random import randint

"""1 -Crie um array V de 38 inteiros aleatórios. Crie outro array W onde cada elemento desse array deve ser cada elemento de V elevado ao cubo (3). Depois imprima na tela:

 - os dois arrays na íntegra

 - o primeiro e o ultimo elemento de cada array

 - do 3ª ao 17ª elemento de ambos arrays

 - metade final dos elementos do array."""


def func_1():
    V = [randint(1, 100) for i in range(38)]
    W = [i**3 for i in V]

    print(V)
    print(W)

    print(V[0])
    print(V[-1])
    print(W[0])
    print(W[-1])

    print(V[2:17])
    print(W[2:17])

    print(V[len(V) // 2 :])
    print(W[len(W) // 2 :])


"""2 - Declare as matrizes a, b e c conforme abaixo. Imprima na tela as três matrizes, linha abaixo de linha. Depois, some os elementos correspondentes das matrizes a e b e armazene o resultado na matriz c (por exemplo: elemento 0x0 da matriz a (33) + elemento 0x0 da matriz b (11) = 44 armazenado no elemento 0x0 da matriz c). Imprima as três matrizes novamente."""


def func_2():
    a = [[33, 44, 55], [22, 77, 11], [99, 10, 17]]
    b = [[11, 12, 13], [98, 97, 91], [14, 12, 72]]
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    print(a)
    print(b)
    print(c)

    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]

    print(a)
    print(b)
    print(c)


"""3 - Solicite ao usuário que digite uma string qualquer. Depois, informe na tela quantas letras "a" e "e" tem nesse string. Dicas: 1) use um laço para percorrer cada item da string. 2) use contadores para "a" e "e". 3) Cada vez que um elemento do array for igual a "a", incrementa o contador de "a" (e assim também para o contador de "e"."""


def func_3():

    countA = 0
    countE = 0
    s = input("Digite um texto qualquer: ")

    for letra in s:
        if letra == "a" or letra == "A":
            countA += 1
        elif letra == "e" or letra == "E":
            countE += 1

    print("Número de letras A: ", countA)
    print("Número de letras E: ", countE)


"""4 - Solicite ao usuário que digite uma string com números e letras. Dessa string, você deverá gerar um array somente com os valores numéricos. Por exemplo: a string "abc12345!?XPTO99" deve resultar no array [1,2,3,4,5,9,9]. Dicas:  1) crie um array vazio auxiliar. 2) use um laço para percorrer cada item da string. 2) Caso o elemento da string for um valor igual a "1" ou "2" ou "3" (assim por diante), inclua ele no array auxiliar. """


def func_4():

    numbers = []
    s = input("digite números e letras: ")
    for caractere in s:
        if (
            caractere == "0"
            or caractere == "1"
            or caractere == "2"
            or caractere == "3"
            or caractere == "4"
            or caractere == "5"
            or caractere == "6"
            or caractere == "7"
            or caractere == "8"
            or caractere == "9"
        ):
            numbers.append(int(caractere))
    print(numbers)


if __name__ == "__main__":
    func_1()
    func_2()
    func_3()
    func_4()
