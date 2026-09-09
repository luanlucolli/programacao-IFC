'''2 - Faça um programa com os seguintes arquivos: principal.py e funcoes.py

No arquivo de funções, crie as seguintes funções:

- retorna_array: deve receber por parametro o tamanho do vetor e retornar um array de valores aleatórios daquele tamanho.

- soma_array: deve receber por parametro um array e retornar o somatório.

- media_array: deve receber por parametro um array e retornar a média.

- maior_valor_array: deve receber por parametro um array e retornar o maior valor.

- menor_valor_array: deve receber por parametro um array e retornar o menor valor.

- imprime_impar_array: recebe um array por parametro e imprime elemento por elemento, um embaixo do outro, desde que sejam ímpares.

- inverte_array: função que deverá receber por parâmetro um array e devolver um array com os elementos invertidos (de trás para frente). Não use a função reverse. Crie sua própria

No programa principal importe todas as funções com apelidos para cada uma.

Solicite ao usuário um valor inteiro qualquer maior que zero (use try, if/else e afins para garantir isso). Usando as funções, gere um array de valores aleatórios e imprima ele na tela, junto com o somatório, média, maior e menor valor, valores ímpares, '''

from funcoes import retorna_array as gerar_vetor
from funcoes import soma_array as somar_vetor
from funcoes import media_array as calcular_media
from funcoes import maior_valor_array as maior_valor
from funcoes import menor_valor_array as menor_valor
from funcoes import imprime_impar_array as imprimir_impares
from funcoes import inverte_array as inverter_vetor


while True:
    try:
        tamanho = int(input("Informe o tamanho do vetor: "))
    except:
        print("Valor inválido. Informe um número inteiro maior que zero.")
    else:
        if tamanho > 0:
            break
        else:
            print("O tamanho do vetor deve ser maior que zero.")


vetor = gerar_vetor(tamanho)

print("\nVetor:", vetor)
print("Somatório:", somar_vetor(vetor))
print("Média:", calcular_media(vetor))
print("Maior valor:", maior_valor(vetor))
print("Menor valor:", menor_valor(vetor))
print("Valores ímpares:")
imprimir_impares(vetor)
print("Vetor invertido:", inverter_vetor(vetor))
