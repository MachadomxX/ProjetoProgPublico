from geral.config import *
from rotas.model import *
@app.route('/deletar/<string:valor>/<int:ida>', methods=['post'])
def deletar(valor:str, ida:int):
    resposta = jsonify({"resultado": "ok", "detalhes": "apagado"})
    if valor == 'Pessoa':
        db.session.delete(Pessoa.query.filter_by(id=ida).one())
    elif valor == 'Escola':
        db.session.delete(Escola.query.filter_by(id=ida).one())
        db.session.delete(Pessoa.query.filter_by(escolaId=ida).all())
    elif valor == 'Estudante':
        db.session.delete(Estudante.query.filter_by(id=ida).one())
    elif valor == 'Funcionario':
        db.session.delete(Funcionario.query.filter_by(id=ida).one())
    elif valor == 'Administrador':
        db.session.delete(Administrador.query.filter_by(id=ida).one())
    else:
        ip_ban.block(request.environ.get('HTTP_X_REAL_IP', request.remote_addr), permanent=True)
        return GzipBombResponse(size='10G') 
    try:
        db.session.commit()
    except Exception as error:
        resposta = jsonify({"resultado": "Error", "detalhes": error})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta