# Uma sequência de bytes representando a palavra 'Hello'
# Tipo bytes são imutáveis
dados_1 = b'\x48\x65\x6c\x6c\x6f'
print(dados_1)  # Saída: b'Hello'
print(type(dados_1))  # Saída: <class 'bytes'>

# Um bytearray com a sequência de bytes 'Hello'
# Tipo de dados bytearray são mutáveis
dados_2 = bytearray(b'\x48\x65\x6c\x6c\x6f')
print(dados_2)  # Saída: bytearray(b'Hello')

# Alterando o primeiro byte para o valor
# hexadecimal 0x41 (representa o caractere 'A')
dados_2[0] = 0x41
print(dados_2)  # Saída: bytearray(b'Aello')
print(type(dados_2))  # Saída: <class 'bytearray'>
