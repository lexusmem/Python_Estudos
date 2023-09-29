import re

email1 = "11234-1234 é o meu número de celular"
email2 = 'meu número de celular é 96176-1340'
email3 = 'celular 96176-1340 é meu número'
email4 = 'asdfasdfad 16176-1340 fasdfasdfas gjfgkdfhgsfghr'

padrao = "[0-9]{5}[-][0-9]{4}"

retorno = re.search(pattern=padrao, string=email3)

print(retorno.group())
