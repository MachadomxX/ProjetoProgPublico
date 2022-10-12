from geral.config import *
import importModelos
from rotas.listar import *
@app.route('/')
def padrao():
    return 'classe'
app.run(debug=True)