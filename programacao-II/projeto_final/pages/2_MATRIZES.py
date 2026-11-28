import streamlit as st

from funcoes import grava_log as gravaLog
from funcoes import gera_matrix as geraMatrix
from funcoes import soma_media_matriz as somaMediaMatriz

st.title("MATRIZES")
st.write("Informe o tamanho da matriz que será gerada.")

linhas = st.text_input("Número de linhas")
colunas = st.text_input("Número de colunas")

if st.button("Enviar"):
    gravaLog("MATRIZES")

    try:
        linhas = int(linhas)
        colunas = int(colunas)
    except:
        st.write("Digite números inteiros para linhas e colunas.")
    else:
        if linhas > 0 and colunas > 0:
            matriz = geraMatrix(linhas, colunas)
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
