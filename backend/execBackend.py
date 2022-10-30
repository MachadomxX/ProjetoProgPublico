from geral.config import *
import importModelos
from rotas.listar import *
from rotas.cadastrar import *
from rotas.deletar import *
from rotas.atualizar import *
from rotas.login import *

@app.route('/')
def padrao():
    return "<a href='https://github.com/MachadomxX/projetoProgPublico'>https://github.com/MachadomxX/projetoProgPublico</a>"
app.run(debug=False, host= '0.0.0.0')
