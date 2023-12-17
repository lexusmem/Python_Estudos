# Aula sobre pacotes disponíveis em bibliotecas python

# https://pypi.org/

#  pacote instalado para validação de cof
# https://pypi.org/project/validate-docbr/
# pip install validate-docbr
from validate_docbr import CPF
from alura_cpf import Cpf

cpf_alex = '22920975838'
cpf = CPF()

new_cpf = cpf.generate(True)

print(new_cpf)
print(cpf.validate(new_cpf))

print(cpf.validate(cpf_alex))
