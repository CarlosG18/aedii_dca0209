import streamlit as st
from lib_autocomplete.avl import AVLTree
from lib_autocomplete.tratamento import get_text_from_pdf, clean_text
from io import BytesIO

st.title("AUTO COMPLETE")
st.caption("criando um auto complete com a estrutura de dados Árvore AVL")
st.divider()

# inserir o corpus
st.header("Insira o Corpus")
st.caption("faça o upload do arquivo (apenas PDF)")
arquivo = st.file_uploader("envie um arquivo PDF", type="pdf")
if arquivo is not None:
    conteudo = arquivo.read()
    texto = get_text_from_pdf(conteudo)
    palavras_tratadas = clean_text(texto,"portuguese")
    # adicionando as palavras na AVL
    avl = AVLTree()
    for palavra in palavras_tratadas:
        avl.add(palavra)
st.divider()

# input do prefixo
st.header("Insira o prefixo")
st.caption("será retornado uma lista de palavras que começam com o seu prefixo informado")
prefix = st.text_input("insira o seu prefixo")
prefix_on = st.button("obter palavras")

if prefix_on:
    lista_de_palavras = avl.autocomplete(prefix)
    st.write(lista_de_palavras)