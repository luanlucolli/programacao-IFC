import streamlit as st

from funcoes import grava_log as gravaLog
from funcoes import gera_matrix as geraMatrix
from funcoes import soma_media_matriz as somaMediaMatriz

st.title("MATRIZES")
st.write("Informe o tamanho da matriz que será gerada.")

linhas = st.number_input("Número de linhas")
colunas = st.number_input("Número de colunas")

if st.button("Enviar"):
    gravaLog("MATRIZES")

    if linhas > 0 and colunas > 0:
        matriz = geraMatrix(int(linhas), int(colunas))
        soma, media = somaMediaMatriz(matriz)

        st.write("Matriz gerada")
        for linha in matriz:
            textoLinha = ""
            for valor in linha:
                textoLinha += str(valor) + " "
            st.write(textoLinha)

        st.write("Somatório: " + str(soma))
        st.write("Média geral: " + str(media))
    else:
        st.write("Informe números de linhas e colunas maiores que zero.")
