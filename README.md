# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/EdelcioBatista/eventex.svg?branch=master)](https://travis-ci.org/EdelcioBatista/eventex)
[![Code Health](https://landscape.io/github/EdelcioBatista/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/EdelcioBatista/eventex/master)


## Como desenvolver?

1. Crie o repositório
2. Crie um vitualenv com Python3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:edelciobatista/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie um instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force

