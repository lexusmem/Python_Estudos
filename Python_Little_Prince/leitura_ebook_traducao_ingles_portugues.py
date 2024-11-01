import ebooklib
from ebooklib import epub
import re
from gemini import traducao

# endereço do ebook
arquivo_epub = r"C:\Users\lexus\Documents\Estudos\Python_Estudos\Python_Little_Prince\The_Little_Prince_by_Antoine_de_Saint.epub"

# lendo epub e gravando na variavel book
book = epub.read_epub(arquivo_epub)

texto = ""

autor = book.get_metadata('DC', 'creator')
titulo = book.get_metadata('DC', 'title')
data = book.get_metadata('DC', 'date')
print(autor[0][0])
print(titulo[0][0])
print(data[0][0])

all_items = book.get_items()

# for item in all_items:
#     if item.get_type() == 9 and item.get_name() == "OEBPS/part0005.xhtml":
#         print('==================================')
#         print(item.get_name(), item.get_type())
#         print('----------------------------------')
#         print(item.get_body_content().decode('utf-8'))


def extrair_texto_epub(arquivo_epub):
    book = epub.read_epub(arquivo_epub)
    texto_completo = ""
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        texto = item.get_content().decode('utf-8')
        # Remover tags HTML e caracteres especiais
        texto = re.sub('<[^<]+?>', '', texto)
        texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
        # Substituindo pulo de linha por espaços
        texto = texto.replace('\n', ' ')
        # Substituindo mais espaços por um único espaços
        texto = re.sub(r'\s+', ' ', texto)
        # Excluindo números
        texto = re.sub(r'\d+', '', texto)
        # texto = re.sub(r'[^a-zA-Z0-9\s,.!?]', '', texto)
        texto_completo += texto.lower()
    return texto_completo


livro = extrair_texto_epub(arquivo_epub)
livro_split = livro.split()
# print(livro_split)

stop_words = ['the', 'to', 'a', 'i', 'and', 'he', 'you',
              'little', 'is', 'of', 'it', 'not', 'in', 'are', 'my',
              'for', 'me', 'on', 'be', 'at', 'as', 'planet', 'so',
              'one', 'no', 'if', 'all', 'am', 'do', 'prince', 'but', 'with',
              'or', 'an', 'time', 'out', 'chapter', 'oh', 'yes', 'now', 'we',
              'day', 'she', 'your', 'go', 'six', 'boa', 'right', 'wwwpanmacmillancoin',
              'n', 'rr', 'cip', 'g', 'k']

# Contar a frequência de cada palavra
contagem_palavras = {}
for palavra in livro_split:
    if palavra in stop_words:
        continue
    else:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1


# Ordenar por frequência (em ordem decrescente)
palavras_ordenadas = sorted(
    contagem_palavras.items(), key=lambda x: x[1], reverse=True)

# Imprimir as 10 palavras mais frequentes
# for palavra, contagem in palavras_ordenadas[:10]:
#     print(f"{palavra}: {contagem}")

arquivo = open(
    r"C:\Users\lexus\Documents\Estudos\Python_Estudos\Python_Little_Prince\palavras.txt", "a")

# Imprimir as 200 palavras mais frequentes com tradução
for palavra, contagem in palavras_ordenadas[:10]:  # [::-1] - reverso
    translate = traducao(palavra)
    dado = f"{contagem};{palavra};{translate}\n"
    arquivo.write(dado)
    # print(palavra, ';', contagem, ';', translate)
