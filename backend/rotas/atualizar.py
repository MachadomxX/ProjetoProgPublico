from geral.config import *
from geral.converter_data import *
from rotas.model import *
from geral.cripto import *

@app.route("/atualizar/<string:classe>",  methods=['PUT'])
def atualizar(classe:str):
    try:
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        dados = request.get_json(force=True)
        if dados['escolaId'] != None and Escola.query.get(dados['escolaId']) == None:
            resposta =  jsonify({"resultado": "erro", "detalhes": "escola inexistente"})
        else:
            if classe == "Escola":id = dados['id'];escola = Escola.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if escola is None else jsonify({"resultado": "ok", "detalhes": "ok"});escola.escola = dados['escola'];escola.cep = dados['cep'];escola.numero = dados['numero'];escola.telefone = dados['telefone'];db.session.commit();return resposta
            try:  
                dados["data"] = converter_data(dados["data"])
            except:
                resposta = jsonify({"resultado": "Error", "detalhes": 'Data no formato YYYY-MM-DD' })
                return resposta
            if classe == "Pessoa":id = dados['id'];pessoa = Pessoa.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if pessoa is None else jsonify({"resultado": "ok", "detalhes": "ok"});pessoa.nome = dados['nome'];pessoa.idade = dados['idade'];pessoa.email = dados['email'];pessoa.telefone = dados['telefone'];pessoa.data = dados['data'];pessoa.escolaId = dados['escolaId'];db.session.commit();return resposta
            elif classe == "Fucionario":id = dados['id'];funcionario = Funcionario.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if funcionario is None else jsonify({"resultado": "ok", "detalhes": "ok"});funcionario.salario = dados['salario'];funcionario.cargaH = dados['cargaH'];escola.cargos = dados['cargos'];pessoa = Pessoa.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if pessoa is None else jsonify({"resultado": "ok", "detalhes": "ok"});pessoa.nome = dados['nome'];pessoa.idade = dados['idade'];pessoa.email = dados['email'];pessoa.telefone = dados['telefone'];pessoa.data = dados['data'];pessoa.escolaId = dados['escolaId'];db.session.commit();return resposta
            elif classe == "Estudante":id = int(dados['id']);estudante = Estudante.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if estudante is None else jsonify({"resultado": "ok", "detalhes": "ok"});estudante.matricula = dados['matricula'];pessoa = Pessoa.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if pessoa is None else jsonify({"resultado": "ok", "detalhes": "ok"});pessoa.nome = dados['nome'];pessoa.idade = int(dados['idade']);pessoa.email = dados['email'];pessoa.telefone = dados['telefone'];pessoa.data = dados['data'];pessoa.escolaId = dados['escolaId'];db.session.commit();return resposta
            elif classe == "Autenticado":id = dados['id'];autenticado = Autenticado.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if autenticado is None else jsonify({"resultado": "ok", "detalhes": "ok"});autenticado.senha = cifrar(dados['senha']);db.session.commit();return resposta
            elif classe == "Administrador":id = dados['id'];administrador = Administrador.query.get(id);resposta = jsonify({"resultado": "erro", "detalhes": "Objeto não encontrado"}) if administrador is None else jsonify({"resultado": "ok", "detalhes": "ok"});administrador.senha = cifrar(dados['senha']); db.session.commit();return resposta
            else: resposta =  jsonify({"resultado": "erro", "detalhes": "classe não encontrado"})
    except:
        resposta =  jsonify({"resultado": "erro", "detalhes": "algo deu errado"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# curl -X PUT -d '{"id":1, "escola":"IFC", "telefone":11111, "numero":12345, "cep":"123"}' -H "Content-Type:application/json"  http://192.168.0.2:5000/atualizar/Escola