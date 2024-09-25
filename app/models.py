from . import db

class User(db.Model):
    __tablename__ = 'Usuarios'
    
    id = db.Column(db.Integer ,primary_key=True)
    Usuario = db.Column(db.String(80) ,unique=True, nullable=False)
    senha = db.Column(db.String(100) , nullable=False)
    CPF = db.Column(db.String(100),unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.Usuario}>'

class Veicles(db.Model):
    __tablename__ = 'Veicles'
    
    id = db.Column(db.Integer ,primary_key=True)
    Marca = db.Column(db.String(80) , nullable=False)
    Modelo = db.Column(db.String(100) , nullable=False)
    Placa = db.Column(db.String(100), nullable=False)
    Valor = db.Column(db.Float, nullable=False)
    Img = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Veicles {self.Marca}>'

class reserva(db.Model):
    __tablename__ = 'reserva'
    
    id = db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.Date, nullable=False)
    fim = db.Column(db.Date, nullable=False)