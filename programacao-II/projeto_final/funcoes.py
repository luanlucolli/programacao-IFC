from random import randint
from datetime import datetime

"""grava_log: recebe uma mensagem e grava no arquivo prog.log."""


def grava_log(mensagem):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    arquivo = open("prog.log", "a")
    arquivo.write(timestamp + " - " + mensagem + "\n")
    arquivo.close()


"""busca_termo: função que recebe por parâmetro um arquivo para leitura e um termo de busca.
Esta função deve retornar um array com as linhas onde o termo de busca é encontrado."""


def busca_termo(arquivo, termo):
    linhas = arquivo.readlines()
    linhasComTermo = []

    for i in linhas:
        if termo in i:
            linhasComTermo.append(i)

    return linhasComTermo


"""conta_termo: deve receber por parâmetro um array de frases e um termo de busca. Esta
função deve retornar a quantidade de frases onde o termo de busca ocorre."""


def conta_termo(frases, termo):
    frasesComTermo = 0
    for i in frases:
        if termo in i:
            frasesComTermo += 1

    return frasesComTermo


"""conta_vogais_consoantes: deve receber por parâmetro uma frase e retornar a quantidade de
vogais, consoantes, numerais e caracteres especiais"""


def conta_vogais_consoantes(frase):
    vogais = 0
    consoantes = 0
    numerais = 0
    caracteresEspeciais = 0

    for caractere in frase.lower():
        if caractere in "aeiouáàâãéêíóôõúü":
            vogais += 1
        elif caractere in "bcdfghjklmnpqrstvwxyzç":
            consoantes += 1
        elif caractere in "0123456789":
            numerais += 1
        else:
            caracteresEspeciais += 1

    return vogais, consoantes, numerais, caracteresEspeciais


"""gera_array: deve receber por parâmetro três valores: tamanho, valor inicial e final, e retornar
um array do tamanho indicado contendo números aleatórios entre valor inicial e final. Use list
comprehensions."""


def gera_array(tamanho, valorInicial, valorFinal):
    return [randint(valorInicial, valorFinal) for i in range(tamanho)]


"""gera_matrix: deve receber por parâmetro o tamanho da matriz, em linhas e colunas. Deve
retornar uma matriz de números aleatórios entre 100 e 999. Use a função gera_array para
gerar as linhas e adicioná-las à matriz"""


def gera_matrix(linhas, colunas):
    matriz = []

    for i in range(linhas):
        matriz.append(gera_array(colunas, 100, 999))

    return matriz


"""soma_media_matriz: deve receber por parâmetro uma matriz e retornar a soma e a média de
de todos os elementos da matriz passada por parâmetro."""


def soma_media_matriz(matriz):
    soma = 0
    qtdElementos = 0
    media = 0

    for i in matriz:
        for j in i:
            soma += j
            qtdElementos += 1

    if qtdElementos > 0:
        media = soma / qtdElementos

    return soma, media


"""calcula_idade: deve receber por parâmetro uma data (dia/mês/ano de nascimento) em
formato string, converter a data para o formato datetime e retornar a idade em anos e meses
(em formato string)."""


def calcula_idade(dataNasc):
    try:
        nascimento = datetime.strptime(dataNasc, "%d/%m/%Y").date()

    except:
        return "Data inválida. Use o formato dd/mm/aaaa."

    else:
        hoje = datetime.now().date()

        if nascimento > hoje:
            return "A data não pode estar no futuro."

        anos = hoje.year - nascimento.year
        meses = hoje.month - nascimento.month

        if hoje.day < nascimento.day:
            meses -= 1

        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"
