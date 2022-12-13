from geral.config import *
from geral.cripto import *
from geral.converter_data import *
from rotas.model import *
@app.route('/cadastrar/<string:valor>', methods=['POST'])
def cadastrar(valor:str):
    try:
        resposta = jsonify({"resultado": "ok", "detalhes": "cadastrado"})
        dados = request.get_json(force=True)
        dados['escolaId'] = int(dados['escolaId'])
        if dados['escolaId'] != None and Escola.query.get(dados['escolaId']) == None:
            resposta =  jsonify({"resultado": "erro", "detalhes": "escola inexistente"})
        else:
            if valor == 'Escola':
                dados["senha"] = cifrar(dados["senha"])
                dado = Escola(**dados)
            else:
                try:  dados["data"] = converter_data(dados["data"])  
                except: resposta = jsonify({"resultado": "Error", "detalhes": 'Data no formato YYYY-MM-DD' })
                if valor == 'Pessoa':
                    dado = Pessoa(**dados)
                
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
                    dado = Autenticado(**dados)
                else:
                    
                    ip_ban.block(request.environ.get('HTTP_X_REAL_IP', request.remote_addr), permanent=True)
                    return GzipBombResponse(size='10G')

                try:
                    print(db.session.query(Escola).filter_by(email=dados['email']).first())
                    if db.session.query(Escola).filter_by(email=dados['email']).first() is not None:
                        resposta =  jsonify({"resultado": "erro", "detalhes": "Email já existente"})
                    elif (db.session.query(Pessoa).filter_by(email=dados['email']).first()) is not None:  
                        resposta =  jsonify({"resultado": "erro", "detalhes": "Email já existente"})
                    else:
                        db.session.add(dado)
                        db.session.commit()
                except Exception as error:
                    resposta = jsonify({"resultado": "Error", "detalhes": error})
    except  Exception as error:    
        resposta = jsonify({"resultado": "error", "detalhes": error})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
        

    # curl -d '{"escola":"IFC", "telefone":11111, "cep":"123", "numero":12345, "email": "escola@gmail.com", "senha": "a"}' -X POST -H "Content-Type:application/json" localhost:5000/cadastrar/Escola
    # curl http://localhost:5000/cadastrar/Estudante -X POST -d '{"nome": "ihig", "idade": 12,"email": "abc@abc", "telefone": "8576858760", "identidade": "iygf", "data": "2022-12-10", "escolaId": 1, "senha": "senha", "matricula": "aa"}'

