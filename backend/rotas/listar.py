from geral.config import *
from rotas.model import *
@app.route('/listar/<string:valor>', methods=['GET'])
def listar_tudo(valor:str):
    try:
        if valor == 'Pessoa':
            pessoas = db.session.query(Pessoa).all()
        elif valor == 'Escola':
            pessoas = db.session.query(Escola).all()
        elif valor == 'Estudante':
            pessoas = db.session.query(Estudante).all()
        elif valor == 'Funcionario':
            pessoas = db.session.query(Funcionario).all()
        elif valor == 'Administrador':
            pessoas = db.session.query(Administrador).all()
        else:
            ip_ban.block(request.environ.get('HTTP_X_REAL_IP', request.remote_addr), permanent=True)
            return GzipBombResponse(size='10G')
            
        val = [x.json() for x in pessoas]
        resposta = jsonify(val)
        resposta.headers.add("Access-Control-Allow-Origin", 
        "*")    
        return resposta
    except:
        resposta =  jsonify({"resultado": "erro", "detalhes": "algo deu errado"})
        return resposta


# curl http://localhost:5000/listar/Pessoa