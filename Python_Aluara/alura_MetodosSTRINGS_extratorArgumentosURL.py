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
