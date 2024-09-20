import ebooklib
from ebooklib import epub
import string

# with open(r"C:\Users\lexus\Documents\Estudos\Python_Little_Prince\The_Little_Prince_by_Antoine_de_Saint.epub", "r", encoding="utf-8") as arquivo:
#     livro = arquivo.readlines()
#     print(livro)

# Abrir o arquivo EPUB
# book = epub.read_epub(
#     r"C:\Users\lexus\Documents\Estudos\Python_Little_Prince\The_Little_Prince_by_Antoine_de_Saint.epub")

# Acessar o título do livro
# print(book.title)


def remover_stop_words(texto, stop_words):
    """Remove stop words de um texto.

    Args:
        texto: O texto a ser processado.
        stop_words: Uma lista de palavras a serem removidas.

    Returns:
        Uma lista de palavras sem as stop words.
    """

    palavras = texto.split()
    palavras_filtradas = [
        palavra for palavra in palavras if palavra not in stop_words]
    return palavras_filtradas


def contar_palavras(arquivo_epub):
    """Conta a frequência de cada palavra em um arquivo EPUB.

    Args:
        arquivo_epub: O caminho para o arquivo EPUB.

    Returns:
        Um dicionário onde as chaves são as palavras e os valores são as
        frequências.
    """

    book = epub.read_epub(arquivo_epub)
    texto = ""

    # Palavras para ser desconsideradas na lista
    stop_words = ['the', 'div', 'to', 'a', 'i', 'and', 'he', 'you',
                  'little', 'is', 'of', 'was', 'it', 'not', 'in', 'are', 'my',
                  'for', 'me', 'on', 'be', 'at', 'as', 'planet', 'so', 'html',
                  'one', 'no', 'if', 'classclass11‘i', 'alt', 'all', 'am',
                  'classclass11i', 'do', 'prince', 'but', 'with', 'classclass11the',
                  '…', 'or', 'xml', 'version10', 'an', 'time', 'out', 'encodingutf8',
                  'doctype', 'xmlnshttpwwww3org1999xhtml', 'xmlnsepubhttpwwwidpforg2007ops',
                  'epubprefixz3998', 'httpwwwdaisyorgz39982012vocabstructure', 'xmllangen',
                  'princediv', 'classclass4img', 'classclass11he', '‘i', "classclass9div",
                  'classclass5chapteraa', 'classclass3span', 'classclass7chapterspan',
                  'classclass6a', 'bodydiv', 'classclass12divdiv', '–', 'classclass11‘it',
                  'classclass11‘you', 'classclass11‘what', 'classclass11but', 'classclass11and',
                  '…’div', '‘it', 'classclass11‘but', '‘what', 'classclass11‘that', 'classclass15img',
                  'classclass11‘and', '‘you', '‘but', 'stars’div', 'prince’s', 'classclass11so', 'classclass11then',
                  'againdiv', 'saiddiv', 'classclass11‘yes', 'classclass11‘oh', 'classclass8the', 'classclass11‘the', 'classclass11‘hello’',
                  'you’', 'sheep’div', '‘that', 'you’div', '‘the', 'himdiv', 'me’div', 'classclass11‘why',
                  'mean’div', 'classclass11‘yes’', 'planet’div', 'classclass16div', '‘they', '‘if', '…’',
                  'classclass11‘where', 'classclass11when', 'classclass11‘my']

    # Extrai o texto de todas as seções
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        texto += item.get_content().decode('utf-8')

    # Pré-processamento: remove pontuação, números e converte para minúsculas
    texto_limpo = texto.translate(
        str.maketrans('', '', string.punctuation)).lower()

    # Tokenização (dividir em palavras)
    palavras = texto_limpo.split()

    # Contar a frequência de cada palavra
    contagem_palavras = {}
    for palavra in palavras:
        if palavra in stop_words:
            continue
        else:
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    # Ordenar por frequência (em ordem decrescente)
    palavras_ordenadas = sorted(
        contagem_palavras.items(), key=lambda x: x[1], reverse=True)

    return palavras_ordenadas


arquivo = r"C:\Users\lexus\Documents\Estudos\Python_Little_Prince\The_Little_Prince_by_Antoine_de_Saint.epub"
resultado = contar_palavras(arquivo)

# Imprimir as 10 palavras mais frequentes
for palavra, contagem in resultado[:400]:
    print(f"{palavra}: {contagem}", end="; ")
