'''1 - Separando a data da hora no método do datetime:

agora = datetime.now()
data = agora.date()
hora = agora.time()

Imprima na tela a data e hora em separado. 
Abaixo disso, imprima o rótulo de tempo completo do datetime no formato brasileiro (d/m/Y H:M:S) utilizando o strftime.'''

from datetime import datetime

agora = datetime.now()
data = agora.date()
hora = agora.time()

print("Data:", data)
print("Hora:", hora)
print("Data e hora no formato brasileiro:", agora.strftime("%d/%m/%Y %H:%M:%S"))
