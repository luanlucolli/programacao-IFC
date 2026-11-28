import streamlit as st

from funcoes import busca_termo as buscaTermo
from funcoes import conta_termo as contaTermo

st.title("BUSCA NO LOG")

try:
    arquivo = open("prog.log", "r")
    linhas = arquivo.readlines()
    arquivo.close()
except:
    linhas = []

termo = st.text_input("Palavra para pesquisar")

if st.button("Pesquisas"):
    if termo == "":
        st.error("Digite uma palavra para pesquisar.")
    elif len(linhas) == 0:
        st.write("Ainda não existem registros no arquivo de log.")
    else:
        arquivo = open("prog.log", "r")
        linhasEncontradas = buscaTermo(arquivo, termo)
        arquivo.close()
        quantidade = contaTermo(linhas, termo)

        st.subheader("Resultado da busca")
        st.write("Linhas encontradas: " + str(quantidade))
        if quantidade == 0:
            st.write("Nenhuma linha contém essa palavra.")
        else:
            for linha in linhasEncontradas:
                st.write(linha)

st.subheader("Todos os registros")
if len(linhas) == 0:
    st.write("O arquivo prog.log ainda não foi criado ou está vazio.")
else:
    for linha in linhas:
        st.write(linha)
