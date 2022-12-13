from logging import exception
from geral.config import *
from rotas.model import *
from geral.cripto import *


@app.route('/logar', methods=['post'])
def logar():
    def chamar(classe):
        try:
            if (x:= db.session.query(classe).filter_by(id=pessoa.id).first()) is not None:
                if validar_senha(x.senha, dados["senha"]):
                    
                    return True
            else:
                return False
        except:
            return error
    try:
        dados = request.get_json(force=True) 
        try:
            pessoa = db.session.query(Pessoa).filter_by(email=dados['email']).first() or db.session.query(Escola).filter_by(email=dados['email']).first()
            if pessoa is not None:
                if chamar(Administrador) is True:
                    resposta = jsonify({"resultado": "ok", "detalhes": "Administrador"})
                elif chamar(Funcionario) is True:
                    resposta = jsonify({"resultado": "ok", "detalhes": "Funcionario"})
                elif chamar(Estudante) is True:
                    resposta = jsonify({"resultado": "ok", "detalhes": "Estudante"})
                elif chamar(Escola) is True:
                    resposta = jsonify({"resultado": "ok", "detalhes": "Escola"})
                else: 
                    resposta = jsonify({"resultado": "Error", "detalhes": 'usuario ou senha errado'})
            else: 
                resposta = jsonify({"resultado": "Error", "detalhes": 'usuario ou senha errado'})
        except Exception as error:
            resposta = jsonify({"resultado": "Error", "detalhes": error})
    except:
        resposta =  jsonify({"resultado": "erro", "detalhes": "algo deu errado"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta

        # curl -d '{"email":"josilva@gmaial.com", "senha":"1a23"}' -X POST -H "Content-Type:application/json" http://192.168.0.4:5000
        # curl -d '{"email":"escola@gmail.com", "senha":"a"}' -X POST -H "Content-Type:application/json" http://localhost:5000/logar
        
        