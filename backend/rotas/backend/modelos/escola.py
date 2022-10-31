from geral.config import *


class Escola(db.Model):
    # atributos da Classe pessoa que serve apenas para herança
    id = db.Column(db.Integer, primary_key=True)
    escola = db.Column(db.String(254))
    cep = db.Column(db.String(254))
    numero = db.Column(db.Integer)
    telefone = db.Column(db.Integer)
    def json(self):
        return {
            "id": self.id,
            "escola": self.escola,
            "cep": self.cep,
            "numero": self.numero,
            "telefone": self.telefone
        }