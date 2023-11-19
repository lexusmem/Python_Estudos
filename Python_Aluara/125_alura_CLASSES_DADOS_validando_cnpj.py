from alura_cpf_cnpj import CpfCnpj
from validate_cnpj import is_valid


new_cnpj = CpfCnpj(22920975838, 'cnpj')

print(new_cnpj)

# cnpj = '12380933000130'
# mascara = cnpj
# mascara_1 = mascara[:2]  # 12
# mascara_2 = mascara[2:5]  # 380
# mascara_3 = mascara[5:8]  # 933
# mascara_4 = mascara[8:12]  # 0001
# mascara_5 = mascara[-2:]  # 30
# print(f'{mascara_1}.{mascara_2}.{mascara_3}/{mascara_4}-{mascara_5}')
