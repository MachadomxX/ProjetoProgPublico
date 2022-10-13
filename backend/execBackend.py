from geral.config import *
import importModelos
from rotas.listar import *
from rotas.cadastrar import *
@app.route('/')
def padrao():
    return 'classe'
app.run(debug=True, host= '0.0.0.0')

#curl -d '{"escola":"IFC", "telefone":11111, "cep":"123", "numero":12345}' -X POST -H "Content-Type:application/json" localhost:5000/cadastrar/Escola