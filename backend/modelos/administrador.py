from geral.config import *
from modelos.pessoa import Pessoa

class Administrador(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    senha = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity': 'Administrador',
    }

    def __str__(self):
        return super().__str__() + f",{self.senha}"

    def json(self):
        return dict(super().json(), **{"senha": self.senha})