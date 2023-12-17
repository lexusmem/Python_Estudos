import re

email1 = "11234-1234 é o meu número de celular"
email2 = 'meu número de celular é 96176-1340'
email3 = 'celular 6176-1340 é meu número'
email4 = 'asdfasdfad 16176-1340 fasdfasdfas 61761340 gjfgkdfhgsfghr 96176-1340'

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.search(pattern=padrao, string=email4)
print(retorno.group())

retornoAll = re.findall(padrao, email4)
print(retornoAll)
