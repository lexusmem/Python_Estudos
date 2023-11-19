import re
from alura_telefone import TelefoneBr

telefone = '551161761340'

telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto)

# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.findall(padrao, telefone)
# print(resposta)

# resposta_1 = re.search(padrao, telefone)
# print(resposta_1)
# print(resposta_1.group())
# print(resposta_1.group(1))
# print(resposta_1.group(2))
