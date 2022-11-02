from geral.config import *
from modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    salario = db.Column(db.Integer, nullable=False)
    cargaH = db.Column(db.Integer, nullable=False)
    cargos = db.Column(db.String(254), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'Funcionario',
    }

    def __str__(self):
        return super().__str__() + f", {self.salario}, {self.cargaH}, {self.cargos}"

    def json(self):
        return dict(super().json(), **{"salario": self.salario,
                                      "cargaH": self.cargaH,
                                      "cargos":self.cargos 
                                      })