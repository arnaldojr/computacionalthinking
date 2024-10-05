
# ORM (Object-Relational Mapping)

ORM é uma técnica que permite interagir com o banco de dados usando objetos Python em vez de SQL diretamente.

## SQLAlchemy

No Flask, usamos SQLAlchemy para ORM. Já configuramos o SQLAlchemy no tutorial anterior.

## Criando e Consultando Registros

Vamos criar e consultar registros no banco de dados:

```python
from app import db
from app.models import User

# Criando um novo usuário
new_user = User(username='johndoe', email='johndoe@example.com', password='senha123')
db.session.add(new_user)
db.session.commit()

# Consultando usuários
users = User.query.all()
print(users)
```

## Atualizando e Deletando Registros

Você também pode atualizar e deletar registros:

```python
# Atualizando um usuário
user = User.query.filter_by(username='johndoe').first()
user.email = 'newemail@example.com'
db.session.commit()

# Deletando um usuário
db.session.delete(user)
db.session.commit()
```

## Conclusão

Neste tutorial, aprendemos a usar ORM com SQLAlchemy no Flask. No próximo tutorial, veremos como garantir a segurança em aplicações web.
    