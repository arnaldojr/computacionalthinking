## Web Scraping com Beautiful Soup

## Introdução
Vamo utilizar a biblioteca `Beautiful Soup` para realizar raspagem de dados (web scraping) em Python. Beautiful Soup é uma biblioteca que facilita extrair informações de páginas web de maneira eficiente e rápida, ela irá nos ajudar em uma etapa importante de `parse` para transformar os dados recebidos pelo requests. 

## Instalação
Para começar, você precisa ter o Python instalado em sua máquina. Após isso, você pode instalar o Beautiful Soup usando pip, o gerenciador de pacotes do Python:

```bash
pip install beautifulsoup4
```

Além do Beautiful Soup, também precisaremos do `requests` para fazer requisições HTTP:

```bash
pip install requests
```

## Primeiros Passos com Beautiful Soup

Primeiro, vamos importar as bibliotecas necessárias e fazer uma requisição simples para obter o HTML de uma página:

```python
import requests
from bs4 import BeautifulSoup

url = 'https://exemplo.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
```

Aqui, `response.text` contém o HTML da página, que é então analisado pelo Beautiful Soup usando `html.parser`.

## Extraindo Dados
Temos algumas maneiras de explorar essa estrutura de dados:

```python 
soup.title   # retorna a tag title do site

soup.title.string # retorna o valor da tag title 

soup.p   # retorna a tag paragrafo = <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']   # retorna o valor do argumento class = u'title'

soup.a   # retorna o tag hiperlink = <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')  # retorna uma lista com todos os hiperlinks
```

Na raspagem de dados, uma tarefa comum é encontrar todos os URLs contidos nas tags `<a>` de uma página, e pode ser realizado varrendo um laço `for` da seguinte forma:

```python
for link in soup.find_all('a'):
   print(link.get('href'))
```
Da mesma forma podemos querer extrair todos os cabeçalhos `<h1>` de uma página:

```python
headers = soup.find_all('h1')
for header in headers:
    print(header.text)
```

Outra tarefa comum é extrair todo o texto de uma página:

```python
print(soup.get_text())
```

## Aplicações Práticas

### Raspagem de Notícias
Você pode usar Beautiful Soup para construir um agregador de notícias, raspando títulos e links de um portal de notícias:

```python
news_items = soup.find_all('div', class_='news_item')
for item in news_items:
    title = item.find('h2').text
    link = item.find('a')['href']
    print(f'Título: {title}, Link: {link}')
```

### Monitoramento de Preços
Beautiful Soup é excelente para monitorar preços de produtos em e-commerce. Aqui está um exemplo simples:

```python
price = soup.find('span', class_='product-price').text
print(f'Preço atual: {price}')
```

