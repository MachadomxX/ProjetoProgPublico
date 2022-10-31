from logging import exception
from geral.config import *
from rotas.model import *
from geral.cripto import *


@app.route('/logar', methods=['post'])
def logar():
    def chamar(classe):

        if (x:= db.session.query(classe).filter_by(id=pessoa.id).first()) is not None:
            if validar_senha(x.senha, dados["senha"]):
                print(validar_senha(x.senha, dados["senha"]), x.senha, dados["senha"], "\n", cifrar(dados["senha"]))
                return True
        else:
            return False

    dados = request.get_json(force=True) 
    try:
        pessoa = db.session.query(Pessoa).filter_by(email=dados['email']).first()
        if pessoa is not None:
            if chamar(Administrador) is True:
                resposta = jsonify({"resultado": "ok", "detalhes": "Administrador"})
            elif chamar(Funcionario) is True:
                resposta = jsonify({"resultado": "ok", "detalhes": "Funcionario"})
            elif chamar(Estudante) is True:
                resposta = jsonify({"resultado": "ok", "detalhes": "Estudante"})
            else: 
                resposta = jsonify({"resultado": "Error", "detalhes": 'Errado parça'})
        else: 
            resposta = jsonify({"resultado": "Error", "detalhes": 'N'})
    except Exception as error:
        resposta = jsonify({"resultado": "Error", "detalhes": error})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

        # curl -d '{"email":"josilva@gmaial.com", "senha":"1a23"}' -X POST -H "Content-Type:application/json" http://191.52.7.74:5000/logar
        # curl -d '{"email":"abc@abc", "senha":"senha"}' -X POST -H "Content-Type:application/json" http://localhost:5000/logar