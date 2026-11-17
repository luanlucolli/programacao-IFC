'''3 - Solicite ao usuário uma data no formato YYYY/mm/dd. Depois imprima essa data por extenso no formato BR, incluindo o dia da semana. 
Ex: 2026/10/22 resulta em: Quinta, 22 de Outubro de 2026.
Para deixar em portugues, acrescente no inicio do programa:

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')'''

import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

texto_data = input("Digite uma data no formato AAAA/MM/DD: ")
data = datetime.strptime(texto_data, "%Y/%m/%d")

print(data.strftime("%A, %d de %B de %Y."))

'''
- %A: nome completo do dia da semana, como quinta-feira.
- %d: dia do mês com dois dígitos, como 22.
- %B: nome completo do mês, como outubro.
- %Y: ano com quatro dígitos, como 2026.
'''