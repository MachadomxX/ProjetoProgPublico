from geral.config import *
from rotas.model import *
@app.route('/listar/<string:valor>')
def listar_tudo(valor:str):
    if valor == 'Pessoa':
        print(valor)
        pessoas = db.session.query(Pessoa).all()
    elif valor == 'Escola':
        pessoas = db.session.query(Escola).all()
    elif valor == 'Estudante':
        pessoas = db.session.query(Estudante).all()
    elif valor == 'Funcionario':
        pessoas = db.session.query(Funcionario).all()
    elif valor == 'Administrador':
        pessoas = db.session.query(Administrador).all()

    resposta = jsonify([x.json() for x in pessoas])
    resposta.headers.add("Access-Control-Allow-Origin", "*")    
    return resposta
