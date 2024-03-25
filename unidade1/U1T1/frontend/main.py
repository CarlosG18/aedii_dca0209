import streamlit as st
from lib_autocomplete.avl import AVLTree
from lib_autocomplete.tratamento import get_text_from_pdf, clean_text

st.title("AUTO COMPLETE")
st.caption("criando um auto complete com a estrutura de dados Árvore AVL")
st.divider()

# escolher o corpus
st.header("escolha o seu corpus")
st.caption("esse corpus será pré-processado para gerar as palavras")
#pdf = st.file_uploader("carregue seu corpus (apenas PDF)")
livros = {
    "Dom Casmurro": "./datasets/dom_casmurro.pdf",
    "O Conde de Monte Cristo": "./datasets/o_conde_de_monte_cristo.pdf",
    "O Pequeno Principe": "./datasets/pequeno_principe.pdf",
}
select_pdf = st.selectbox("escolha seu livro", livros)
st.divider()
# carregar as palavras
path_pdf = livros[select_pdf]
texto = get_text_from_pdf(path_pdf)
palavras_tratadas = clean_text(texto,"portuguese")

# adicionando as palavras na AVL
avl = AVLTree()
for palavra in palavras_tratadas:
  avl.add(palavra)

# input do prefixo
st.header("Insira o prefixo")
st.caption("será retornado uma lista de palavras que começam com o seu prefixo informado")
prefix = st.text_input("insira o seu prefixo")
prefix_on = st.button("obter palavras")

if prefix_on:
    lista_de_palavras = avl.autocomplete(prefix)
    st.write(lista_de_palavras)
# mostrar as palvras