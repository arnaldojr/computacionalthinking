
# Conexão com Banco de Dados

O Flask pode se conectar a vários bancos de dados. Neste tutorial, vamos usar o SQLite para simplicidade.

## Configurando o Banco de Dados

Crie um arquivo `config.py`:

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Inicializando o Banco de Dados

No `__init__.py` do seu aplicativo:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
```

## Criando um Modelo

Crie um modelo para a tabela de usuários:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```

## Criando o Banco de Dados

Para criar o banco de dados:

```python
from app import app, db

with app.app_context():
    db.create_all()
```

## Conclusão

Neste tutorial, aprendemos a conectar nossa aplicação Flask a um banco de dados usando SQLAlchemy. No próximo tutorial, veremos como usar ORM (Object-Relational Mapping).
    