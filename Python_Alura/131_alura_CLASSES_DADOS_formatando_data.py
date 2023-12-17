# from datetime import datetime, timedelta
from alura_datas import DatasBr


cadastro = DatasBr()
print(cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro.format_data())

# retorna hora e data exata
# print(datetime.today())

# strftime retorna hora e data formatada
# hoje = datetime.today()
# hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
# print(hoje)
# print(hoje_formatada)

# print('-----------------------')
# hoje = datetime.today()
# semana = hoje.weekday()
# print(semana)
