from random import randint

"""cria_matriz: recebe por parâmetro a quantidade de linhas e colunas e retorna uma matriz preenchida com valores aleatórios entre 0 e 100. (Dica: gere cada linha como um vetor e adicione eles em uma matriz)"""


def cria_matriz(linhas, colunas):
    matriz = []

    for i in range(linhas):
        matrizAux = []
        for j in range(colunas):
            matrizAux.append(randint(0, 99))
        matriz.append(matrizAux)

    return matriz


"""soma_linha: recebe por parâmetro uma matriz e retorna um array com a soma dos elementos de cada uma das linhas."""


def soma_linha(matriz):
    somaElementos = []

    for i in range(len(matriz)):
        somaTemp = 0
        for j in range(len(matriz[i])):
            somaTemp += matriz[i][j]

        somaElementos.append(somaTemp)
    return somaElementos


"""maior_menor_matriz: recebe por parâmetro uma matriz e retorna o maior e o menor valor dessa matriz.
"""


def maior_menor_matriz(matriz):
    menor = 999
    maior = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    print(menor)


matrizTeste = [[2, 2, 2], [3, 3, 3, 3], [4, 4]]

maior_menor_matriz(matrizTeste)
