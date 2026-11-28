import streamlit as st

from funcoes import grava_log as gravaLog
from funcoes import conta_vogais_consoantes as contaVogaisConsoantes

st.title("TEXTOS")
st.write("Informe o caminho de um arquivo de texto do computador.")

caminho = st.text_input("Caminho do arquivo", placeholder="Exemplo: textos.txt")

if st.button("Enviar"):
    gravaLog("TEXTOS")

    if caminho == "":
        st.error("Informe o caminho de um arquivo.")
    else:
        try:
            arquivo = open(caminho, "r")
            texto = arquivo.read()
            arquivo.close()
        except:
            st.error("Não foi possível abrir esse arquivo. Confira o caminho informado.")
        else:
            vogais, consoantes, numerais, especiais = contaVogaisConsoantes(texto)
            st.subheader("Resultado")
            st.write("Vogais: " + str(vogais))
            st.write("Consoantes: " + str(consoantes))
            st.write("Numerais: " + str(numerais))
            st.write("Caracteres especiais: " + str(especiais))
