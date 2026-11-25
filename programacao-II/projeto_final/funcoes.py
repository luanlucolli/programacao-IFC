from random import randint
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

"""grava_log: função que deve receber por parâmetro uma mensagem e gravar no arquivo
“prog.log” no formato “ timestamp | mesagem“."""


def grava_log(mensagem):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    arquivo = open("prog.log", "a")
    arquivo.write(timestamp + " | " + mensagem + "\n")
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
    caracteresesEspeciais = 0

    for caractere in frase.lower():
        if caractere in "aeiou":
            vogais += 1
        elif caractere in "bcdfghjklmnpqrstvwxyz":
            consoantes += 1
        elif caractere in "0123456789":
            numerais += 1
        else:
            caracteresesEspeciais += 1

    return vogais, consoantes, numerais, caracteresesEspeciais


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
    for i in matriz:
        for j in i:
            soma += j
            qtdElementos += 1

    media = soma / qtdElementos
    return soma, media


"""calcula_idade: deve receber por parâmetro uma data (dia/mês/ano de nascimento) em
formato string, converter a data para o formato datetime e retornar a idade em anos e meses
(em formato string)."""


def calcula_idade(dataNasc):
    dataNasc = datetime.strptime(dataNasc, "%d/%m/%Y")
    agora = datetime.now()

    anos = agora.year - dataNasc.year
    meses = agora.month - dataNasc.month

    return f"{anos} anos e {meses} meses"


print(calcula_idade("03/02/2006"))
