from geral.config import *
from rotas.model import *
@app.route('/validar', methods=['POST'])
def validar():
    try:
        dados = request.get_json(force=True) 
        try: 
            if db.session.query(Pessoa).filter_by(email=dados['email']).first() is not None:
                print(db.session.query(Pessoa).filter_by(email=dados['email']).first().cargo)
                if db.session.query(Pessoa).filter_by(email=dados['email']).first().cargo is not None:

                    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
            elif db.session.query(Escola).filter_by(email=dados['email']).first():
                if dados['cargo'] == 'Escola':
                    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
                
            else:
                resposta = jsonify({"resultado": "nao", "detalhes": "nao"})
        except: resposta = jsonify({"resultado": "no", "detalhes": "no"}); resposta.headers.add("Access-Control-Allow-Origin", "*");resposta.headers.add("Access-Control-Allow-Credentials", "true"); return resposta
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        resposta.headers.add("Access-Control-Allow-Credentials", "true")
        return resposta
    except Exception  as error:
        resposta =  jsonify({"resultado": "erro", "detalhes":   'error'})
        return resposta

