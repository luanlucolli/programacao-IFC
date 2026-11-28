from datetime import datetime
import streamlit as st

from funcoes import grava_log as gravaLog
from funcoes import calcula_idade as calculaIdade

st.title("IDADE")
st.write("Informe seu nome e seu ano de nascimento.")
st.write("Estimativa: considera 1º de janeiro, às 00h, como data de nascimento.")

nome = st.text_input("Nome")
anoAtual = datetime.now().year
anoNascimento = st.number_input(
    "Ano de nascimento", min_value=1900, max_value=anoAtual, value=2000, step=1
)

if st.button("Enviar"):
    gravaLog("IDADE")

    if nome == "":
        st.error("Informe seu nome.")
    else:
        nascimento = datetime.strptime(
            "01/01/" + str(int(anoNascimento)), "%d/%m/%Y"
        )
        agora = datetime.now()
        diferenca = agora - nascimento

        idade = calculaIdade("01/01/" + str(int(anoNascimento)))
        anos = agora.year - int(anoNascimento)
        meses = anos * 12 + agora.month - 1
        dias = diferenca.days
        horas = diferenca.days * 24 + agora.hour

        st.subheader("Resultado")
        st.write(nome + ", você está vivo há " + idade + ".")
        st.write("Isso corresponde a:")
        st.write("a)", meses, "meses")
        st.write("b)", dias, "dias")
        st.write("c)", horas, "horas")
