
## Introdução ao Flask

Flask é um microframework para a web escrito em Python. É leve e flexível, tornando-se uma escolha popular para desenvolvedores que buscam uma ferramenta rápida e eficiente para criar aplicações web.

## Instalação

Para começar, você precisa instalar o Flask. Você pode fazer isso usando pip:

```bash
pip install Flask
```

## Primeiro Aplicativo 😁

Aqui está um exemplo simples de um aplicativo Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo, criamos uma instância do Flask, definimos uma rota para a URL raiz (`/`) e uma função que retorna uma string quando essa rota é acessada. Finalmente, executamos o aplicativo no modo de debug.

## Estrutura de um Projeto Flask

Uma estrutura típica de projeto Flask pode se parecer com isto:

```
myproject/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── venv/
├── .flaskenv
├── config.py
└── run.py
```

- `app/__init__.py`: Inicializa a aplicação Flask.
- `app/routes.py`: Define as rotas da aplicação.
- `app/templates/`: Contém os templates HTML.
- `.flaskenv`: Configurações de ambiente.
- `config.py`: Configurações da aplicação.
- `run.py`: Script para rodar a aplicação.

## Conclusão

Essa foi uma introdução ao Flask. Nos próximos tutoriais, exploraremos como criar rotas, lidar com formulários, renderizar templates e conectar a um banco de dados.
