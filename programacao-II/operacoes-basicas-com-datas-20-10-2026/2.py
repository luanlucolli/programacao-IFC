"""2 - Solicite ao usuário para digitar duas datas e converta-as para o formato datetime (usando strptime). Imprima a diferença entre essas duas datas. Depois disto, imprima ambas as datas na tela no formato brasileiro (d/m/Y H:M:S) utilizando o strftime."""

from datetime import datetime

data1 = input("Digite a primeira data e hora (DD/MM/AAAA HH:MM:SS): ")
data2 = input("Digite a segunda data e hora (DD/MM/AAAA HH:MM:SS): ")

data1 = datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")
data2 = datetime.strptime(data2, "%d/%m/%Y %H:%M:%S")


if data1 > data2:
    diferenca = data1 - data2
else:
    diferenca = data2 - data1

print(diferenca)

formato_brasileiro = "%d/%m/%Y %H:%M:%S"
print("Primeira data:", data1.strftime(formato_brasileiro))
print("Segunda data:", data2.strftime(formato_brasileiro))
