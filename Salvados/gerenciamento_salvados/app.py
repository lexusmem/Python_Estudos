from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados SQLite


def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Tabela de salvados
    c.execute('''CREATE TABLE IF NOT EXISTS salvados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sinistro TEXT NOT NULL,
        placa TEXT NOT NULL,
        modelo TEXT,
        status TEXT DEFAULT 'Removido',
        data_remocao TEXT,
        data_transferencia_seguradora TEXT,
        data_vistoria1 TEXT,
        data_vistoria2 TEXT,
        custo REAL,
        data_leilao TEXT,
        valor_arremate REAL,
        comprador TEXT,
        data_transferencia_comprador TEXT
    )''')
    # Tabela de opções de status
    c.execute('''CREATE TABLE IF NOT EXISTS status_opcoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )''')
    # Inserir status iniciais (se a tabela estiver vazia)
    c.execute("SELECT COUNT(*) FROM status_opcoes")
    if c.fetchone()[0] == 0:
        status_iniciais = ['Removido', 'Em Remoção',
                           'Vendido', 'Aguardando Vistoria']
        c.executemany("INSERT INTO status_opcoes (nome) VALUES (?)", [
                      (s,) for s in status_iniciais])
    conn.commit()
    conn.close()

# Função para obter lista de status disponíveis


def get_status_opcoes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT nome FROM status_opcoes")
    status = [row[0] for row in c.fetchall()]
    conn.close()
    return status

# Rota para a página inicial (listagem de salvados)


@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM salvados")
    salvados = c.fetchall()
    conn.close()
    return render_template('index.html', salvados=salvados)

# Rota para adicionar ou editar um salvado


@app.route('/salvado', methods=['GET', 'POST'])
def salvado():
    status_opcoes = get_status_opcoes()
    if request.method == 'POST':
        sinistro = request.form['sinistro']
        placa = request.form['placa']
        modelo = request.form['modelo']
        status = request.form['status']
        data_remocao = request.form['data_remocao']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''INSERT INTO salvados (sinistro, placa, modelo, status, data_remocao)
                     VALUES (?, ?, ?, ?, ?)''', (sinistro, placa, modelo, status, data_remocao))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('salvado_form.html', status_opcoes=status_opcoes)

# Rota para atualizar status de um salvado


@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    status_opcoes = get_status_opcoes()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        status = request.form['status']
        if status == 'Transferência Concluída':
            data_transferencia_seguradora = request.form['data_transferencia_seguradora']
            c.execute("UPDATE salvados SET status=?, data_transferencia_seguradora=? WHERE id=?",
                      (status, data_transferencia_seguradora, id))
        elif status == 'Vistorias Concluídas':
            data_vistoria1 = request.form['data_vistoria1']
            data_vistoria2 = request.form['data_vistoria2']
            c.execute("UPDATE salvados SET status=?, data_vistoria1=?, data_vistoria2=? WHERE id=?",
                      (status, data_vistoria1, data_vistoria2, id))
        elif status == 'Custo Definido':
            custo = request.form['custo']
            c.execute(
                "UPDATE salvados SET status=?, custo=? WHERE id=?", (status, custo, id))
        elif status == 'Vendido':
            data_leilao = request.form['data_leilao']
            valor_arremate = request.form['valor_arremate']
            comprador = request.form['comprador']
            c.execute("UPDATE salvados SET status=?, data_leilao=?, valor_arremate=?, comprador=? WHERE id=?",
                      (status, data_leilao, valor_arremate, comprador, id))
        elif status == 'Transferência Finalizada':
            data_transferencia_comprador = request.form['data_transferencia_comprador']
            c.execute("UPDATE salvados SET status=?, data_transferencia_comprador=? WHERE id=?",
                      (status, data_transferencia_comprador, id))
        else:
            c.execute("UPDATE salvados SET status=? WHERE id=?", (status, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    c.execute("SELECT * FROM salvados WHERE id=?", (id,))
    salvado = c.fetchone()
    conn.close()
    return render_template('salvado_form.html', salvado=salvado, status_opcoes=status_opcoes)

# Nova rota para gerenciar status


@app.route('/gerenciar_status', methods=['GET', 'POST'])
def gerenciar_status():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        acao = request.form['acao']
        if acao == 'inserir':
            novo_status = request.form['novo_status']
            try:
                c.execute(
                    "INSERT INTO status_opcoes (nome) VALUES (?)", (novo_status,))
                conn.commit()
            except sqlite3.IntegrityError:
                pass  # Ignora se já existir
        elif acao == 'excluir':
            status_id = request.form['status_id']
            c.execute("DELETE FROM status_opcoes WHERE id=?", (status_id,))
            conn.commit()
        elif acao == 'alterar':
            status_id = request.form['status_id']
            novo_nome = request.form['novo_nome']
            c.execute("UPDATE status_opcoes SET nome=? WHERE id=?",
                      (novo_nome, status_id))
            conn.commit()

    c.execute("SELECT * FROM status_opcoes")
    status_opcoes = c.fetchall()
    conn.close()
    return render_template('gerenciar_status.html', status_opcoes=status_opcoes)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
