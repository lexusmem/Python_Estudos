def remover_stop_words(texto, stop_words):
    """Remove stop words de um texto.

    Args:
        texto: O texto a ser processado.
        stop_words: Uma lista de palavras a serem removidas.

    Returns:
        Uma lista de palavras sem as stop words.
    """

    palavras = texto.split()
    palavras_filtradas = [
        palavra for palavra in palavras if palavra not in stop_words]
    return palavras_filtradas[0]


# Exemplo de uso:
stop_words = ['a', 'o', 'e', 'que', 'um', 'de', 'em', 'para']
texto = "Este é um exemplo de texto com muitas palavras comuns."
resultado = remover_stop_words(texto, stop_words)
print(resultado)
print(type(resultado))
