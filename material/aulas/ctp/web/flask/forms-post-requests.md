
# Formulários e Requisições POST

Os formulários permitem que os usuários enviem dados para o servidor. As requisições POST são usadas para enviar esses dados.

## Criando um Formulário HTML

Aqui está um exemplo de um formulário HTML:

```html
<form action="/submit" method="post">
    <label for="name">Nome:</label>
    <input type="text" id="name" name="name">
    <input type="submit" value="Enviar">
</form>
```

## Lidando com Requisições POST

No Flask, você pode lidar com requisições POST usando `request.form`:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Nome recebido: {name}"

if __name__ == '__main__':
    app.run(debug=True)
```

## Protegendo Formulários com CSRF

Para proteger seus formulários contra ataques CSRF, você pode usar a extensão Flask-WTF:

```bash
pip install Flask-WTF
```

Exemplo de uso:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitButton
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    submit = SubmitButton('Enviar')
```

## Conclusão

Neste tutorial, aprendemos a criar e lidar com formulários e requisições POST no Flask. No próximo tutorial, veremos como renderizar templates.
    