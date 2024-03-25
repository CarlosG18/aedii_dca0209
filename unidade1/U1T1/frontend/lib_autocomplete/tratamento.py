import nltk
import fitz
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

def get_text_from_pdf(file_name):
  '''
    função que obtem o conteudo de um pdf.

      - parâmetros:
       - file_name: nome do arquivo.

      - retorno:
       - a função retorna o texto obtido.
  '''

  texto = ""
  pdf = fitz.open(file_name)
  for pagina in pdf:
      texto += pagina.get_text()
  pdf.close()
  return texto

def remove_letras_repetidas(palavra):
    """
        função que remove letras repetidas de uma palavra.

        - parâmetros:
            - palavra: palavra que contém letras repetidas

        - retorno:
            - nova_palavra: palavra inical sem a ocorrência de letras repetidas
    """
    if not palavra:
        return ""

    nova_palavra = palavra[0]
    for letra in palavra[1:]:
        if letra != nova_palavra[-1]:
            nova_palavra += letra
    return nova_palavra

def tem_letra_repetida(palavra):
    """
        função que verifica se a palavra possui letras repetidas

        - parâmetros:
            - palavra: palavra para ser checada se possui letra repetida

        - retorno:
            - Bool
    """
    letras_vistas = set()
    for letra in palavra:
        if letra in letras_vistas:
            return True
        letras_vistas.add(letra)
    return False

def clean_text(text, language):
  """
    função que obtém um vetor com todas as palavras do texto.

      - parâmetros:
        - text: string que possui o conteudo do texto.
        - language: idioma das palavras

      - retorno:
        - texto_tratado: a funçao retorna uma lista com apenas palavras do texto passado como parâmetro.
  """
  # retirando hifen em palavras que ocorreu por causa da limitação do espaço
  text = text.replace('-\n','')

  # obtendo apenas palavras minusculas e excluindo números e caracteres especiais
  texto_tratado = regexp_tokenize(text.lower(), r'\b[A-Za-z]+\b', gaps=False)

  # obtendo todas as palavras de parada (stopwords)
  stopwords_ = set(stopwords.words(language))
  # obtendo todas as palavras que não são stopwords e que seu tamanho são maiores que 2
  texto_tratado = [word for word in texto_tratado if word not in stopwords_ and len(word) > 2]

  #ajustando palavras com letras repetidas:
  for index,palavra in enumerate(texto_tratado):
    if tem_letra_repetida(palavra):
      texto_tratado[index] = remove_letras_repetidas(palavra)

  return set(texto_tratado)
