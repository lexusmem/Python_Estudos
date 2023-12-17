# escrever - write
# arquivo = open("palavras.txt", "w")

# ler arquivo - read
# arquivo = open("palavras.txt", "r")

# ler adicionar - append
# arquivo = open("palavras.txt", "a")

arquivo = open("palavras.txt", "w")
arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.close()

arquivo = open("palavras.txt", "a")
arquivo.write("morango\n")
arquivo.write("maça\n")
arquivo.close()
