from validate_docbr import CPF
from validate_cnpj import is_valid


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == 'cpf':
            if self.cpf_e_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF Inválido!!')
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ Inválido!!')
        else:
            raise ValueError('Tipo de Documento Inválido!!')

    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos Inválidos!!')

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            return is_valid(cnpj)
        else:
            raise ValueError('Quantidade de dígitos Inválidos!!')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = self.cnpj
        mascara_1 = mascara[:2]
        mascara_2 = mascara[2:5]
        mascara_3 = mascara[5:8]
        mascara_4 = mascara[8:12]
        mascara_5 = mascara[-2:]
        return (f'{mascara_1}.{mascara_2}.{mascara_3}/{mascara_4}-{mascara_5}')

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()
