'''2 - Copie as linhas abaixo e salve como um arquivo de texto chamado "exemplo_log.txt".

2026-10-24 14:40:05 [INFO] Usuario jonh.armless fez login com sucesso.
2026-10-24 14:41:10 [WARN] Tentativa de conexão lenta ao banco de dados (tempo: 1200ms).
2026-10-24 14:42:00 [ERROR] NullPointerException na classe CheckoutService.java:45.
2026-10-24 14:43:00 [INFO] Usuario chuck.norris fez login com sucesso.
2026-10-24 14:40:05 [INFO] Usuario jonh.armless fez logoff com sucesso.

Faça um programa que leia o conteúdo do arquivo de log e crie um novo arquivo "exemplo_log_numerado.txt" onde deverá ser acrescentado no início de cada linha o número da linha. O resultado deverá ser algo como:
1. 2026-10-24 14:40:05 [INFO] Usuario jonh.armless fez login com sucesso.
2. 2026-10-24 14:41:10 [WARN] Tentativa de conexão lenta ao banco de dados (tempo: 3 - 1200ms).
3. 2026-10-24 14:42:00 [ERROR] NullPointerException na classe CheckoutService.java:45.
...

Feito isso, exiba o conteúdo do novo arquivo criado na tela.'''

arquivo = open("exemplo_log.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

arquivo_numerado = open("exemplo_log_numerado.txt", "w")
for i in range(len(linhas)):
    arquivo_numerado.write(str(i + 1) + ". " + linhas[i])
arquivo_numerado.close()

arquivo_numerado = open("exemplo_log_numerado.txt", "r")
conteudo = arquivo_numerado.read()
print(conteudo)
arquivo_numerado.close()
