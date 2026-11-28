import os
from datetime import datetime
import streamlit as st

from funcoes import grava_log as gravaLog
from funcoes import busca_termo as buscaTermo
from funcoes import conta_termo as contaTermo
from funcoes import conta_vogais_consoantes as contaVogaisConsoantes
from funcoes import gera_array as geraArray
from funcoes import gera_matrix as geraMatrix
from funcoes import soma_media_matriz as somaMediaMatriz
from funcoes import calcula_idade as calculaIdade

st.title("Projeto Final")

st.write("Luan Gustavo Luçolli")

st.image("luan_gustavo_lucolli.png")

st.write("Informações do projeto")
st.write("Nome: Luan Gustavo Luçolli")
st.write("Semestre: 2º semestre")
st.write("Curso: Redes de Computadores")
st.write("Disciplina: Programação II")

linkCurriculo = "https://www.linkedin.com/in/luan-gustavo-lucolli/"
st.write("[Abrir currículo](" + linkCurriculo + ")")

st.write("Acesso ao sistema")
agora = datetime.now()
st.write("Data e hora: " + agora.strftime("%d/%m/%Y %H:%M:%S"))
st.write("Tipo de sistema: " + os.name)
