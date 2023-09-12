p1 = {3, 5}
p2 = {4, 6}
p3 = {5, 7}
line = [p1, p2, p3]
print(p1)
print(type(p1))
print(line)
print(type(line))
print(line[0])
print(type(line[0]))

palavra = []

palavra.append('banana')
palavra.append('abacaxi')

print(palavra)
print(type(palavra))

nova_tuple = tuple(palavra)
print(nova_tuple)
print(type(nova_tuple))

nova_lista = list(nova_tuple)
print(nova_lista)
print(type(nova_lista))

nova_str = str(nova_lista)
print(nova_str)
print(type(nova_str))
