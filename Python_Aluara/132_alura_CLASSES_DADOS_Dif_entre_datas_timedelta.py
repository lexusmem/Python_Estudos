from datetime import datetime, timedelta
from alura_datas import DatasBr

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1, hours=20)
# print(amanha - hoje)

cadastro = DatasBr()
print(cadastro.tempo_cadastro())
print(type(cadastro.tempo_cadastro()))
