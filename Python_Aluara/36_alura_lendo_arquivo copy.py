# escrever - write
# arquivo = open("palavras.txt", "w")

# ler arquivo - read
# arquivo = open("palavras.txt", "r")

# adicionar - append
# arquivo = open("palavras.txt", "a")

arquivo = open("palavras.txt", "r")
arquivo.read()

for linha in arquivo:
    print(linha)

arquivo.close()

arquivo = open("palavras.txt", "r")
linha = arquivo.readline()
print(linha)

# removendo o \n do final da string
print(linha, end="")
# ou
print(linha.strip())
