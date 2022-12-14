from modelos.pessoa import Pessoa
from geral.config import *
from modelos.funcionario import Funcionario

class Autenticado(Funcionario):
    id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), primary_key=True)
    senha = db.Column(db.Text, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'Autenticado',
    }
    def __str__(self):
        return super().__str__() + f",{self.senha}"

    def json(self):
        return dict(super().json(), **{"senha": self.senha})