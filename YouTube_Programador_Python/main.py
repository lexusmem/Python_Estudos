from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route


# Programador Python
# Desenvolvimento Web com Flask e Python
# https://youtube.com/playlist?list=PL39zbyHjgjrbsP3xFSc-YH-6FN8WNpglh&si=Nit-C1cn3pnBTu5P

# Parei
#

# Inicialização
app = Flask(__name__)

# rotas
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

# execução
app.run(debug=True)
