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
        elif classe == "Fucionario":id = dados['id'];funcionario = Funcionario.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if funcionario is None else jsonify({"resultado": "ok", "detalhes": "ok"});funcionario.salario = dados['salario'];funcionario.cargaH = dados['cargaH'];escola.cargos = dados['cargos'];db.session.commit()
        elif classe == "Estudante":id = dados['id'];estudante = Estudante.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if estudante is None else jsonify({"resultado": "ok", "detalhes": "ok"});estudante.matricula = dados['matricula'];estudante.senha = dados['senha'];db.session.commit()
        elif classe == "Autenticado":id = dados['id'];autenticado = Autenticado.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if autenticado is None else jsonify({"resultado": "ok", "detalhes": "ok"});autenticado.senha = dados['senha'];db.session.commit()
        elif classe == "Administrador":id = dados['id'];administrador = Administrador.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if administrador is None else jsonify({"resultado": "ok", "detalhes": "ok"});admiministrador.senha = dados['senha']; db.session.commit()
       
        else: resposta =  jsonify({"resultado": "erro", "detalhes": "classe não encontrado"})
    return resposta

#curl -X PUT -d '{"id":1, "escola":"IFC", "telefone":11111, "numero":12345, "cep":"123"}' -H "Content-Type:application/json"  http://192.168.0.2:5000/atualizar/Escola
