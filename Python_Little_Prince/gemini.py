from deep_translator import GoogleTranslator


def traducao(word):
    tradutor = GoogleTranslator(source='en', target='pt')
    resultado = tradutor.translate(word)
    return resultado


one = traducao('nothing')
print(one)
