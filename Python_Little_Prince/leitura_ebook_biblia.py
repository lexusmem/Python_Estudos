import ebooklib
from ebooklib import epub
import re

# endereço do ebook
arquivo_epub = r"C:\Users\lexus\Documents\Estudos\Python_Estudos\Python_Little_Prince\pg62383-images-3.epub"

# lendo epub e gravando na variavel book
book = epub.read_epub(arquivo_epub)

texto = ""

all_items = book.get_items()

# for item in all_items:
#     if item.get_type() == 9 and item.get_name() == "6964025759731777341_62383-h-1042.htm.xhtml":
#         print('==================================')
#         print(item.get_name(), item.get_type())
#         print('----------------------------------')
#         print(item.get_body_content().decode('utf-8'))

# for item in all_items:
#     print(item.get_name(), item.get_type())
#     print('----------------------------------')


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

stop_words = ['a', 'o', 'e', 'que', 'um', 'de', 'em', 'para',
              'os', 'no', 'do', 'cap', 'da', 'se', 'as', 'dos', 'com', 'ao',
              'porque', 'seu', 'sua', 'por', 'como', 'seus', 'i', 'na',
              'elle', 'sobre', 'terra', 'filhos', 'disse', 'eu', 'ii', 'ento', 'me', 'tambem',
              'aos', 'mas', 'todos', 'pois', 'meu', 'te', 'ver', 'teu', 'assim', 'porm', 'deu',
              'suas', 'das', 'nem', 'ser', 'tua', 'vs', 'uma', 'at', 'ou', 'minha', 'vos', 'mat', 'isa',
              'elles', 'todo', 'est', 'mais', 'nos', 'tu', 'lhe', 'mim', 'dizendo', 'ti', 'quando', 'mo',
              'exo', 'joo', 'eis', 's', 'toda', 'jer', 'pelo', 'quem', 'teus', 'luc', 'so', 'pae', 'cor',
              'foi', 'este', 'entre', 'diz', 'num', 'todas', 'chr', 'sam', 'rom', 'era', 'gen', 'jos', 'ha',
              'fez', 'pela', 'j', 'tinha', 'psa', 'foram']

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
for palavra, contagem in palavras_ordenadas[:100]:
    print(f"{palavra}: {contagem}")
    # print(f"{palavra}", end=',')


# # Escrever em um arquivo as palavras
# arquivo = open(
#     r"C:\Users\lexus\Documents\Estudos\Python_Estudos\Python_Little_Prince\biblia.txt", "a")

# # Imprimir as 200 palavras mais frequentes e escrever no arquivo
# for palavra, contagem in palavras_ordenadas[:200]:  # [::-1] - reverso
#     dado = f"{contagem};{palavra}\n"
#     arquivo.write(dado)
