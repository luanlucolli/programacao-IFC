"""No arquivo funcoes_str.py, crie as seguintes funções:"""

"""inverte_str: recebe uma string por parâmetro e retorna a string invertida. Não use reverse. Monte sua própria lógica com laço."""


def inverte_str(texto):
    textoInvertido = ""
    for i in range(len(texto) - 1, -1, -1):
        textoInvertido += texto[i]
    return textoInvertido


"""e_palindromo: recebe uma string por parâmetro e retorna True se ela for um palíndromo (ler de trás para frente é igual, ignorando espaços) e False caso contrário."""


def e_palindromo(texto):
    textoInvertido = ""
    textoNormal = ""

    for i in range(len(texto)):
        if texto[i] != "":
            textoNormal += texto[i]

    for i in range(len(texto) - 1, -1, -1):
        if texto[i] != "":
            textoInvertido += texto[i]

    if textoNormal == textoInvertido:
        return True
    else:
        return False

'''localiza_caracter: recebe uma string por parametro e pergunta ao usuário para digitar uma letra. Retorna True se localizar a letra e False se não localizar.'''
def localiza_caracter(texto):
    letraDesejada = input("digite uma letra: ")
    letraDesejada = letraDesejada.lower()
    achou = False
    
    for letra in texto.lower():
        if letra == letraDesejada:
            achou = True
    
    return achou

print(localiza_caracter("marrocos"))
