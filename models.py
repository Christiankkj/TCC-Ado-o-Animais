from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
from flask_login import UserMixin

class TipoUsuarioEnum(enum.Enum):
    pessoa = "pessoa"
    empresa = "empresa"

class TipoAnimalEnum(enum.Enum):
    gato = "gato"
    cachorro = "cachorro"

class Usuario(Base, UserMixin):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    tipo = Column(Enum(TipoUsuarioEnum), nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    nome_dono = Column(String(100), nullable=True)  # só se for empresa

    animais = relationship("AnimaisAdocao", back_populates="usuario")


class AnimaisAdocao(Base):
    __tablename__ = 'animais_adocao'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))
    tipo = Column(Enum(TipoAnimalEnum), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="animais")