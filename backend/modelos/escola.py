from geral.config import *


class Escola(db.Model):
    # atributos da Classe pessoa que serve apenas para herança
    id = db.Column(db.Integer, primary_key=True)
    escola = db.Column(db.String(254), nullable=False)
    cep = db.Column(db.String(254), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    senha = db.Column(db.Text, nullable=False)
    def json(self):
        return {
            "id": self.id,
            "escola": self.escola,
            "cep": self.cep,
            "numero": self.numero,
            "telefone": self.telefone,
            "email": self.email
        }