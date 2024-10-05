
# Rotas e Requisições GET

No Flask, as rotas são definidas para mapear URLs para funções no seu código. As requisições GET são usadas para solicitar dados de um servidor.

## Definindo Rotas

Para definir uma rota, você usa o decorador `@app.route`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Página Inicial"

@app.route('/about')
def about():
    return "Sobre Nós"

if __name__ == '__main__':
    app.run(debug=True)
```

## Parâmetros de URL

Você pode adicionar parâmetros às suas rotas:

```python
@app.route('/user/<username>')
def show_user(username):
    return f"Usuário: {username}"
```

## Requisições GET

Para acessar dados enviados via URL, você pode usar `request.args`:

```python
from flask import request

@app.route('/search')
def search():
    query = request.args.get('q')
    return f"Resultados da pesquisa para: {query}"
```

## Conclusão

Neste tutorial, vimos como definir rotas e lidar com requisições GET no Flask. No próximo tutorial, exploraremos formulários e requisições POST.
    