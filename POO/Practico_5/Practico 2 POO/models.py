from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import values

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    clave = db.Column(db.String(80), nullable=False)
    #referencias
    receta = db.relationship('Receta', backref='usuario', cascade="all, delete-orphan")


class Receta(db.Model):
    __tablename__ = "receta"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tiempo = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    elaboracion = db.Column(db.String(120), nullable=False)
    cantidadmegusta = db.Column(db.Integer, nullable=False)
    #referencias
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    ingredientes = db.relationship('Ingredientes', backref='receta', cascade="all, delete-orphan")



class Ingredientes(db.Model):
    __tablename__ = "ingredientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad = db.Column(db.String(80), nullable=False)
    #referencias
    recetaid = db.Column(db.Integer, db.ForeignKey('receta.id'), nullable=False)