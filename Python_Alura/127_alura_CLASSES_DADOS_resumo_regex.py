import re

# Expressão regulares - Regex

# servem para encontrar padrões dentro de textos


padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())


padrao_1 = "[0-9][a-z]{2}[0-9]"
texto_1 = "123 1ac2 1cc aa1"
resposta_1 = re.search(padrao_1, texto_1)
print(resposta_1.group())

# padrão para email:
padrao_email = "\w{1,50}.\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto_2 = "asdfasdffas asdfasdfasdfasda alex.sousa@alseg.com.br sdfasdfasd asdfasdfas"
resposta_2 = re.search(padrao_email, texto_2)
print(resposta_2.group())

# padrão celular
padra_molde = '(xx)aaaa-wwww'
padrao_celular = "[0-9]{0,2}[0-9]{4,5}[0-9]{4}"
texto_3 = ' eu tenho meu numero 11961761340 de celular'
resposta_3 = re.findall(padrao_celular, texto_3)
print(resposta_3)
