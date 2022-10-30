from os import error
from geral.config import *
from rotas.model import *
<<<<<<< Updated upstream
from hashlib import blake2b
from datetime import date

def converter_data(data):
    d = data.split("-")
    return date(int(d[0]), int(d[1]), int(d[2]))

def cifrar(senha):
    h = blake2b()
    em_bytes = bytes(senha, encoding= 'utf-8')
    h.update(em_bytes)
    return h.hexdigest()

def valida_senha(cifrado, senha_fornecida):
    fornecida = cifrar(senha_fornecida)
    if cifrado == fornecida:
         return True
    return False

=======
from datetime import date
from geral.cripto import *

def converter_data(data):
    d = data.split("-")
    if (int(d[0])>1950) and (int(d[0])<date.year) and (int(d[1])>0) and (int(d[1])<13) and (int(d[2])>0) and (int(d[2])<31):
        return date(int(d[0]), int(d[1]), int(d[2]))
    else:
        return error
>>>>>>> Stashed changes

@app.route('/cadastrar/<string:valor>', methods=['post'])
def cadastrar(valor:str):
    resposta = jsonify({"resultado": "ok", "detalhes": "cadastrado"})
<<<<<<< Updated upstream
    dados = request.get_json(force=True)  
    dados["data"] = converter_data(dados["data"])    
=======
    dados = request.get_json(force=True)
    try:  
        dados["data"] = converter_data(dados["data"])  
    except Exception as error:
        return 'Data no formato YYYY-MM-DD vagaba'
>>>>>>> Stashed changes
    if valor == 'Pessoa':
        dado = Pessoa(**dados)
    elif valor == 'Escola':
        dado = Escola(**dados)
    elif valor == 'Estudante':
<<<<<<< Updated upstream
        
=======
>>>>>>> Stashed changes
        dados["senha"] = cifrar(dados["senha"])
        dado = Estudante(**dados)
    elif valor == 'Funcionario':
        dado = Funcionario(**dados)
    elif valor == 'Administrador':
        dados["senha"] = cifrar(dados["senha"])
        dado = Administrador(**dados)
    elif valor == 'Autenticado':
        dados["senha"] = cifrar(dados["senha"])
        dado = Autenticado(**dados)
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
    #curl -d '{"escola":"IFC", "telefone":11111, "cep":"123", "numero":12345}' -X POST -H "Content-Type:application/json" localhost:5000/cadastrar/Escola





'''
<<<<<<< Updated upstream
curl http://localhost:5000/cadastrar/Estudante -X POST -H "Content-Type:application/json" -d '{"nome": "ihig", "idade": 12,
"email": "abc@abc", "telefone": "8576858760", "identidade": "iygf", "data": "2022-12-20", "escolaId": 1, "matricula": "iuktfduktdutfd", "senha": "senha"}'
=======
curl http://localhost:5000/cadastrar/Estudante -X POST -H "Content-Type:application/json" -d '{"nome": "ihig", "idade": 12,"email": "abc@abc", "telefone": "8576858760", "identidade": "iygf", "data": "2022-12-20", "escolaId": 1, "matricula": "iuktfduktdutfd", "senha": "senha"}'
>>>>>>> Stashed changes
'''