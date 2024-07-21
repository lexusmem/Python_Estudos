from flask import Flask, url_for, render_template

# Inicialização
app = Flask(__name__)


# rotas
@app.route('/')
def ola_mundo():
    titulo = 'Gestão de Usuários'
    usuarios = [
        {'nome': 'Alex', 'membro_ativo': True},
        {'nome': 'Sheila', 'membro_ativo': False},
        {'nome': 'Sabrina', 'membro_ativo': True},
    ]
    # utilizando JINJA
    return render_template("index.html", titulo=titulo, usuarios=usuarios)


'''
        <p>Suave de Boa!</p>
        <a href='{url_for('pagina_sobre')}'>Página Sobre</a>
'''


@app.route('/sobre')
def pagina_sobre():
    return f'''
        <a href='{url_for('ola_mundo')}'>Página Principal</a>
        <h1>Teste da Página Sobre</h1>
        <b>Programado Pyhotn</b>: assista os videos no
        <a href='https://youtube.com/@programadospyhton'>Canal no YouTube</a>

'''


# execução
app.run(debug=True)
