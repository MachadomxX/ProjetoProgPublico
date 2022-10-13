from geral.config import *
import importModelos
from rotas.listar import *
from rotas.cadastrar import *
from rotas.deletar import *
@app.route('/')
def padrao():
    return 'classe'
app.run(debug=True, host= '0.0.0.0')
