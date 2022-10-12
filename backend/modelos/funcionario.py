from geral.config import *
from modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    salario = db.Column(db.Integer)
    cargaH = db.Column(db.Integer)
    cargos = db.Column(db.String(254))
    __mapper_args__ = {
        'polymorphic_identity': cargos,
    }

    def __str__(self):
        return super().__str__() + f", {self.salario}, {self.cargaH}"

    def json(self):
        return dict(super().json(), **{"salario": self.salario,
                                      "cargaH": self.cargaH
                                      })