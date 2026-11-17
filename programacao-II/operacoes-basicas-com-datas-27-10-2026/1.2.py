"""1 - Faça um programa que solicite ao usuário um número de 1 a 5. Se digitar 0 o programa encerra. Outras opções devem ser inválidas. Para cada valor de 1 a 5, deverão ser apresentados ao usuário uma frase motivacional (caso você não tenha criatividade, procure no Instagram "dicas do esqueleto", rsrsrs). O programa deverá gerar um arquivo chamado "opcoes.log" e registrar dentro dele todas as opções que o usuário digitou (com o timestamp do momento), no seguinte formato:
2026-10-31 09:26:30.153498 - Opção 2
2026-10-31 09:26:31.161776 - Opção Inválida
2026-10-31 09:26:33.101112 - Opção 1"""

from datetime import datetime

rascunho = ""

while True:
    opcao = input("Digite uma opção de 1 a 5 (0 para sair): ")
    agora = datetime.now()

    if opcao == "1":
        print("Acredite em você e continue tentando!")
        registro = "Opção 1"
    elif opcao == "2":
        print("Cada passo já é um progresso.")
        registro = "Opção 2"
    elif opcao == "3":
        print("Você é capaz de aprender coisas novas.")
        registro = "Opção 3"
    elif opcao == "4":
        print("Não desista: bons resultados levam tempo.")
        registro = "Opção 4"
    elif opcao == "5":
        print("O seu esforço de hoje ajuda a construir o seu amanhã.")
        registro = "Opção 5"
    elif opcao == "0":
        registro = "Opção 0"
    else:
        print("Opção inválida.")
        registro = "Opção Inválida"

    rascunho += agora.strftime("%Y-%m-%d %H:%M:%S.%f") + " - " + registro + "\n"

    if opcao == "0":
        break
arquivo = open("opcoes.log", "w")
arquivo.write(rascunho)
arquivo.close()
