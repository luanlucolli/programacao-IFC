from fn_esp import countVogais as ctv
from fn_esp import countConsoantes as ctc
from fn_esp import countNumeros as ctn
from fn_esp import countCaracterEspecial as cte
from fn_esp import indicesVogais as iv
from fn_esp import indicesConsoantes as ic
from fn_esp import indicesNumeros as ino
from fn_esp import indicesCaracterEspecial as ice
from fn_esp import arrayIsPair as aip


texto = input("Digite uma frase: ")

print("Quantidade de vogais:", ctv(texto))
print("Quantidade de consoantes:", ctc(texto))
print("Quantidade de números:", ctn(texto))
print("Quantidade de caracteres especiais:", cte(texto))

print("Índices das vogais:", iv(texto))
print("Índices das consoantes:", ic(texto))
print("Índices dos números:", ino(texto))
print("Índices dos caracteres especiais:", ice(texto))

print("Par ou ímpar para cada número:")
aip(texto)
