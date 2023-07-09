# sinistro = float(input('Informe o Valor de Sinistro: '))
# print(f'O valor de sinistro é de {sinistro: ,.2f}')
# percentual_sinistro = float (0.4)
# premio_cobrar = sinistro / percentual_sinistro
# print (f'O prêmio a ser cobrado é de {premio_cobrar: ,.2f} para que o sinistro fique a 40%.')
# nova_sinistralidade = sinistro / premio_cobrar
# print (f'Nova Sinistralidade {nova_sinistralidade: .2%}.')

def calcular_sinistralidade(valor_sinistro, premio_recebido):
    sinistralidade = valor_sinistro / premio_recebido
    return sinistralidade


print('===Calcular Sinistralidade===\n')
sin = float(input('Informe o valor do sinistro: '))
pr = float(input('Informe o valor do prêmio: '))
sintr = calcular_sinistralidade(sin, pr)
print(f'A sinitralidade apurada é {sintr: .2%}.\n')


def calcular_premio_sinistro(valor_sinistro_inf, precentual_sin_desejado):
    valor_pr_cobrar = valor_sinistro_inf / (precentual_sin_desejado/100)
    return valor_pr_cobrar


print('===Prêmio a Ser Cobrado por Valor de Sinistro===\n')
sin_inf = float(input('Informe o valor do sinistro: '))
perc_sin = float(input('Informe o percentual de sinistro desejado: '))
pr_cob = calcular_premio_sinistro(sin_inf, perc_sin)
print(
    f'O prêmio a ser cobrado para uma sinistralidade de{(perc_sin/100): .2%} é R${pr_cob: ,.2f}.\n')
