from random import randint

x = [2, 1, 4, 3]


def retorna_array(length):
    return [randint(1, 100) for i in range(length)]


def soma_array(vetor):
    return sum(vetor)


def media_array(vetor):
    return sum(vetor) / len(vetor)


def maior_valor_array(vetor):
    return max(vetor)


def menor_valor_array(vetor):
    return min(vetor)


def imprime_impar_array(vetor):
    for i in range(len(vetor)):
        if vetor[i] % 2 != 0:
            print(vetor[i])


def inverte_array(vetor):
    '''vetor_invertido = []
    for i in range(len(vetor) - 1, -1, -1):
        vetor_invertido.append(vetor[i])'''
    vetor.reverse()

    return vetor

x = retorna_array()
print(x)