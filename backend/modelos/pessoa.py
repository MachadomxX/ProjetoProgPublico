from geral.config import *
from modelos.escola import Escola

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.Integer)
    email = db.Column(db.String(254), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    identidade = db.Column(db.Text)
    cargo = db.Column(db.String(50))
    data = db.Column(db.Date)
    
    escolaId = db.Column(db.Integer, db.ForeignKey(Escola.id))
    escola = db.relationship("Escola")

    __mapper_args__ = {
        'polymorphic_identity': 'Pessoa',
        'polymorphic_on': cargo
    }

    def __str__(self):
        return self.nome + "[id="+str(self.id) + "], " +\
            str(self.idade) + "," + self.email + "," + self.telefone +\
            ", " + self.identidade + ", " + f'{self.data.day}/{self.data.month}/{self.data.year}' +\
            ", " + self.escola.escola + ", " + self.cargo

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "telefone": self.telefone,
            "identidade": self.identidade,
            "cargo": self.cargo,
            "data": f'{self.data.day}/{self.data.month}/{self.data.year}',
            "escola": self.escola.escola
        }