from geral.config import *
from modelos.pessoa import Pessoa
class Estudante(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    matricula = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    __mapper_args__ = {
        'polymorphic_identity': 'Estudante',
    }

    def __str__(self):
        return super().__str__() + f", {self.matricula},{self.senha}"

    def json(self):
        return dict(super().json(), **{"matricula": self.matricula,
                                      "senha": self.senha
                                      })