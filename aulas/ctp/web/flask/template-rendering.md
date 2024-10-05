
# Renderização de Templates

O Flask usa o mecanismo de templates Jinja2 para renderizar templates HTML. Isso permite que você crie páginas HTML dinâmicas.

## Criando um Template

Crie um arquivo `index.html` no diretório `templates`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Bem-vindo, {{ name }}!</h1>
</body>
</html>
```

## Renderizando um Template

Use `render_template` para renderizar o template:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

## Templates Heredados

Você pode criar layouts base e herdar de outros templates:

`base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

`index.html`:

```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h1>Bem-vindo, {{ name }}!</h1>
{% endblock %}
```

## Conclusão

Neste tutorial, aprendemos a renderizar templates no Flask. No próximo tutorial, exploraremos como conectar sua aplicação a um banco de dados.
    