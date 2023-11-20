from datetime import datetime, timedelta
from alura_datas import DatasBr

# retorna hora e data exata
print(datetime.today())

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
