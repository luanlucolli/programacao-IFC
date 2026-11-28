from datetime import datetime
import streamlit as st

from funcoes import grava_log as gravaLog
from funcoes import calcula_idade as calculaIdade

st.title("IDADE")
st.write("Informe seu nome e seu ano de nascimento.")
st.write("Estimativa: considera 1º de janeiro, às 00h, como data de nascimento.")

nome = st.text_input("Nome")
anoAtual = datetime.now().year
anoNascimento = st.text_input("Ano de nascimento")

if st.button("Enviar"):
    gravaLog("IDADE")

    if nome == "":
        st.write("Informe seu nome.")
    else:
        try:
            anoNascimento = int(anoNascimento)
        except:
            st.write("Digite um ano de nascimento válido.")
        else:
            if anoNascimento < 1900 or anoNascimento > anoAtual:
                st.write("Informe um ano entre 1900 e " + str(anoAtual) + ".")
            else:
                nascimento = datetime.strptime(
                    "01/01/" + str(anoNascimento), "%d/%m/%Y"
                )
                agora = datetime.now()
                diferenca = agora - nascimento

                idade = calculaIdade("01/01/" + str(anoNascimento))
                anos = agora.year - anoNascimento
                meses = anos * 12 + agora.month - 1
                dias = diferenca.days
                horas = diferenca.days * 24 + agora.hour

                st.write("Resultado")
                st.write(nome + ", você está vivo há " + idade + ".")
                st.write("Isso corresponde a:")
                st.write("a) " + str(meses) + " meses")
                st.write("b) " + str(dias) + " dias")
                st.write("c) " + str(horas) + " horas")
