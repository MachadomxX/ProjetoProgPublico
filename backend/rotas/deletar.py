from logging import exception
from geral.config import *
from rotas.model import *
@app.route('/deletar/<string:valor>/<int:ida>', methods=['post'])
def deletar(valor:str, ida:int):
    resposta = jsonify({"resultado": "ok", "detalhes": "apagado"})
    try:
        if valor == 'Pessoa':
            db.session.delete(Pessoa.query.filter_by(id=ida).one())
        elif valor == 'Escola':
            db.session.delete(Escola.query.filter_by(id=ida).one())
            for x in Pessoa.query.filter_by(escolaId=ida).all():db.session.delete(x)
        elif valor == 'Estudante':
            db.session.delete(Estudante.query.filter_by(id=ida).one())
        elif valor == 'Funcionario':
            db.session.delete(Funcionario.query.filter_by(id=ida).one())
        elif valor == 'Administrador':
            db.session.delete(Administrador.query.filter_by(id=ida).one())
        else:
            ip_ban.block(request.environ.get('HTTP_X_REAL_IP', request.remote_addr), permanent=True)
            return GzipBombResponse(size='10G')
    except Exception as error:
        resposta = jsonify({"resultado": "Error", "detalhes": error})
    try:
        db.session.commit()
    except Exception as error:
        resposta = jsonify({"resultado": "Error", "detalhes": error})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# curl -X POST http://192.168.0.4:5000/deletar/Pessoa/0