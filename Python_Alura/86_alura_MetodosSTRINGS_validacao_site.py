class ExtratorArgumentosURL:
    def __init__(self, url):
        if self.urlEhvalida(url):
            self.url = url.lower()
        else:
            raise LookupError('URL Inválida!!!!!')

    # Método estático

    @staticmethod
    def urlEhvalida(url):
        if url and url.startswith('https://bytebank.com'):
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = 'moedadestino='.lower()

        indiceInicialOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalOrigem = self.encontraIndiceFinal(indiceInicialOrigem)
        moedaOrigem = self.url[indiceInicialOrigem:indiceFinalOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalOrigem = self.encontraIndiceFinal(indiceInicialOrigem)
            moedaOrigem = self.url[indiceInicialOrigem:indiceFinalOrigem]

        indiceInicialDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalDestino = self.encontraIndiceFinal(indiceInicialDestino)
        moedaDestino = self.url[indiceInicialDestino:indiceFinalDestino]
        return moedaOrigem, moedaDestino

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def encontraIndiceFinal(self, indiceInicial):
        return self.url.find("&", indiceInicial)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)


# ============================
url = 'https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino='\
      'dolar&valor=1500'

argumentoUrl = ExtratorArgumentosURL(url)
print(argumentoUrl.url)

moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()
valor = argumentoUrl.extraiValor()
print(f'A moeda de origem é o {moedaOrigem}.')
print(f'A moeda de destino é o {moedaDestino}.')
print(f'O valor é {valor}.')
