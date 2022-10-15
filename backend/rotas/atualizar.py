from geral.config import *
from rotas.model import *

@app.route("/atualizar/<string:classe>",  methods=['put'])
def atualizar(classe:str):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json(force=True) 
    if 'id' not in dados:
            resposta = jsonify({"resultado": "erro", "detalhes": "Atributo id não encontrado"})
            return resposta
    else:
        if classe == "Escola":id = dados['id'];escola = Escola.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if escola is None else jsonify({"resultado": "ok", "detalhes": "ok"});escola.escola = dados['escola'];escola.cep = dados['cep'];escola.numero = dados['numero'];escola.telefone = dados['telefone'];db.session.commit()
        elif classe == "Pessoa":id = dados['id'];pessoa = Pessoa.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if pessoa is None else jsonify({"resultado": "ok", "detalhes": "ok"});pessoa.nome = dados['nome'];pessoa.idade = dados['idade'];pessoa.email = dados['email'];pessoa.telefone = dados['telefone'];pessoa.data = dados['data'];pessoa.escolaId = dados['escolaId'];db.session.commit()
        else: resposta =  jsonify({"resultado": "erro", "detalhes": "classe não encontrado"})
    return resposta

#curl -X PUT -d '{"id":1, "escola":"IFC", "telefone":11111, "numero":12345, "cep":"123"}' -H "Content-Type:application/json"  http://192.168.0.2:5000/atualizar/Escola
