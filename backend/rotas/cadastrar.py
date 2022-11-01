from geral.config import *
from geral.cripto import *
from geral.converter_data import *
from rotas.model import *
@app.route('/cadastrar/<string:valor>', methods=['post'])
def cadastrar(valor:str):
    resposta = jsonify({"resultado": "ok", "detalhes": "cadastrado"})
    dados = request.get_json(force=True) 
    try:  
        dados["data"] = converter_data(dados["data"])  
    except:
        return 'Data no formato YYYY-MM-DD vagaba' 
    if valor == 'Pessoa':
        dado = Pessoa(**dados)
    elif valor == 'Escola':
        dado = Escola(**dados)
    elif valor == 'Estudante':
        dados["senha"] = cifrar(dados["senha"])
        dado = Estudante(**dados)
    elif valor == 'Funcionario':
        dado = Funcionario(**dados)
    elif valor == 'Administrador':
        dados["senha"] = cifrar(dados["senha"])
        dado = Administrador(**dados)
    elif valor == 'Autenticado':
        dados["senha"] = cifrar(dados["senha"])
        dado = Administrador(**dados)
    else:
        ip_ban.block(request.environ.get('HTTP_X_REAL_IP', request.remote_addr), permanent=True)
        return GzipBombResponse(size='10G') 
    try:
        db.session.add(dado)
        db.session.commit()
    except Exception as error:
        resposta = jsonify({"resultado": "Error", "detalhes": error})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
    # curl -d '{"escola":"IFC", "telefone":11111, "cep":"123", "numero":12345}' -X POST -H "Content-Type:application/json" localhost:5000/cadastrar/Escola
    # curl http://localhost:5000/cadastrar/Estudante -X POST -H "Content-Type:application/json" -d '{"nome": "ihig", "idade": 12,"email": "aabzc@abc", "telefone": "8576858760", "identidade": "iygf", "data": "20222-12-20", "escolaId": 1, "matricula": "iuktfduktdutfd", "senha": "senha"}'
