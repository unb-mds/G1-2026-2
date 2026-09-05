from datetime import date

import sqlmodel
from pydantic import BaseModel,validator,field_validator,EmailStr
from sqlmodel import Field, SQLModel
from typing import Literal

class Usuario(SQLModel,table = True):
    id : int |None = Field(default=None,
                         primary_key=True)
    email : EmailStr
    nome : str
    perfil : str
    status : Literal["Online","Offline","Aparecer Offline","Ausente"]
    criado_em : date
    atualizado_em : date

class Curso(SQLModel,table = True):
    id: int | None = Field(default=None,
                           primary_key=True)
    nome : str
    sigla : str # Coloque str temporariamnete,depois podemos criar um tipo especifico para ela
    ativo : bool

class Disciplina(SQLModel,table = True):
    id: int | None = Field(default=None,
                           primary_key=True)

    curso_id : list[int]  #coloque como lista pois uma disciplina pode pertencer a varios cursos,
    codigo : int
    nome : str
    periodo : date
    ativo : bool

#implemntar Conteudo academico
#implemntar Contribuicao

class FonteInstitucional(SQLModel,table = True):
    id: int | None = Field(default=None,
                           primary_key=True)
    nome : str
    conteudo_id : int
    disciplina : Disciplina
    tipo : str # colocar depois a tipagem definitiva depois
    frequencia_verificacao : str #colocar depois a tipagem definitiva
    estado : Literal["ativa","pausada","indisponivel"]
    ultima_verificacao : date