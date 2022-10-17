from geral.config import *
import importModelos
from rotas.listar import *
from rotas.cadastrar import *
from rotas.deletar import *
from rotas.atualizar import *

@app.route('/')
def padrao():
    return 'https://github.com/MachadomxX/projetoProgPublico'
app.run(debug=True, host= '0.0.0.0')
