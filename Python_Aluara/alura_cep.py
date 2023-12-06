import requests


class BuscaEndereco:

    def __init__(self, cep_):
        cep = str(cep_)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Inválido!')

    def __str__(self):
        return f'{self.format_cep()} - {self.acessa_via_cep()}'

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        bairro = dados['bairro']
        cidade = dados['localidade']
        uf = dados['uf']
        return f'{bairro}, {cidade}, {uf}'
