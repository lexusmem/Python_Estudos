class ExtratorArgumentosURL:
    def __init__(self, url):
        if self.urlEhvalida(url):
            self.url = url
        else:
            raise LookupError('URL Inválida!!!!!')

    # Método estático

    @staticmethod
    def urlEhvalida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = 'moedadestino'

        indiceInicialDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalDestino = self.encontraIndiceFinal(indiceInicialDestino)

        indiceInicialOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalOrigem = self.encontraIndiceFinal(indiceInicialOrigem)

        moedaOrigem = self.url[indiceInicialOrigem:indiceFinalOrigem]
        moedaDestino = self.url[indiceInicialDestino:indiceFinalDestino]
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) + 1

    def encontraIndiceFinal(self, indiceInicial):
        return self.url.find("&", indiceInicial)
