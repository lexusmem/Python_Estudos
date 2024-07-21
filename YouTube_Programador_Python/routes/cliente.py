from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

'''
Rota de Clientes
-/(home)
    -/clientes/ (GET) - Listar os Clientes
    -/clientes/ (POST) - Inserir clientes no servidor
    -/clientes/new (GET) - renderizar o formulário para um cliente
    -/clientes/<id> (GET) - obter dados de um cliente
    -/clientes/<id>/edit (GET) - renderizar um formulário para editar cliente
    -/clientes/<id>/update (PUT) - atualizar dados para clientes
    -/clientes/<id>/delete (DELETE) - deleta registro do usuário
'''


@cliente_route.route('/')
def lista_clientes():
    ''' Listar os clientes '''
    return render_template('lista_cliente.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    ''' Inserir dados dos clientes '''

    data = request.json

    novo_cliente = {
        'id': len(CLIENTES) + 1,
        'nome': data['nome'],
        'email': data['email'],
    }

    CLIENTES.append(novo_cliente)

    return render_template('item_cliente.html', cliente=novo_cliente)


@cliente_route.route('/new')
def form_cliente():
    ''' Formulário para cadastrar um cliente '''
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    ''' Exibir detalhes de um cliente '''

    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]

    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    ''' Formulário para editar um cliente '''
    cliente = None

    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    ''' Atualizar dados de um cliente '''
    cliente_editado = None
    # obter dados do formulário de edição
    data = request.json

    # obter usuario pelo id
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c

    # editar usuário
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    ''' Deletar dados de um cliente '''
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]

    return {'deleted': 'ok'}
