# Tradutor de numeros inteiros para extenso

Este projeto é resultado de um teste elaborado para avaliação em vaga de programador back-end.

# Pré-requisitos:

Para facilitar a analise e teste do projeto , o mesmo foi dockerizado , sendo assim pode usar seu respectivo dockerfile , caso contrário será imprescindivel ter instalado:

[Como instalar docker](https://docs.docker.com/install/)

[Como instalar pipenv](https://github.com/pypa/pipenv)

1. Python 3.8
2. Flask
3. Uwsgi
4. Pipenv

# Instalando o projeto:

### Via docker:

```console
docker build -t flask-project .
```

### Via Pipenv:

```console
pipenv --three
pipenv install flask uwsgi
```

# Rodando o projeto:

### Via docker:

```console
docker run -p 5000:5000 flask-project
```

### Via Pipenv:

```console
pipenv shell
uwsgi --ini app/wsgi.ini
```

# Briefing do teste :

Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne um JSON cuja chave extenso seja a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].

Exemplos:

```console
curl http://localhost:3000/1
```
retorno esperado:  { "extenso": "um" }
```console
curl http://localhost:3000/-1042
```
retorno esperado:   { "extenso": "menos mil e quarenta e dois" }
```console
curl http://localhost:3000/94587
```
retorno esperado:   { "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }