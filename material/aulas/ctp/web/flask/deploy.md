
# Deploy de Aplicações

Fazer o deploy de uma aplicação Flask envolve várias etapas, desde a configuração do servidor até a implantação do código.

## Escolhendo um Servidor

Você pode usar servidores como Gunicorn ou uWSGI para servir sua aplicação Flask. Aqui está um exemplo usando Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

## Configurando um Servidor Web

Use um servidor web como Nginx para lidar com requisições HTTP e encaminhá-las para sua aplicação Flask:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Uso de Docker

Você pode usar Docker para criar um contêiner da sua aplicação:

```dockerfile
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
```

Construa e execute o contêiner:

```bash
docker build -t myflaskapp .
docker run -d -p 8000:8000 myflaskapp
```

## Conclusão

Neste tutorial, aprendemos a fazer o deploy de uma aplicação Flask usando Gunicorn, Nginx e Docker. Esses são apenas alguns métodos de deploy; há muitas outras ferramentas e técnicas que você pode explorar.
    