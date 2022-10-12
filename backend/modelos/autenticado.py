from geral.config import *
from modelos.funcionario import Funcionario

class Autenticado(Funcionario):
    senha = db.Column(db.String(254))

    def __str__(self):
        return super().__str__() + f",{self.senha}"

    def json(self):
        return dict(super().json(), **{"senha": self.senha})