
# Segurança em Aplicações Web

A segurança é uma preocupação crítica no desenvolvimento de aplicações web. Aqui estão algumas práticas recomendadas para proteger suas aplicações Flask.

## Proteção Contra CSRF

CSRF (Cross-Site Request Forgery) é um ataque onde comandos não autorizados são transmitidos a partir de um usuário em quem a aplicação web confia. Use Flask-WTF para proteger seus formulários:

```python
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
```

## Segurança de Senhas

Nunca armazene senhas em texto plano. Use uma biblioteca como `werkzeug.security` para hashear senhas:

```python
from werkzeug.security import generate_password_hash, check_password_hash

hashed_password = generate_password_hash('mypassword')
check_password_hash(hashed_password, 'mypassword')  # Retorna True se a senha corresponder
```

## Configurações de Segurança

Certifique-se de usar configurações de segurança apropriadas em produção:

```python
app.config['SESSION_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
```

## Autenticação e Autorização

Use extensões como Flask-Login para gerenciar a autenticação de usuários:

```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
```

## Conclusão

Neste tutorial, abordamos práticas recomendadas de segurança para aplicações Flask. No próximo tutorial, veremos como fazer o deploy de uma aplicação Flask.
    