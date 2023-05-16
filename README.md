# Django vs Flask: Comparando frameworks

Este projeto faz parte do vídeo **Django vs Flask: Comparando frameworks**
do [canal **Backend em Ação**](https://www.youtube.com/@backendemacao). 

Considere nos apoiar inscrevendo-se e
reagindo aos nosso vídeos no YouTube. Obrigado.

## Rodando aplicação Django

1. Entre na pasta `django`

2. Crie e ative um [ambiente virtual com venv](https://docs.python.org/3/library/venv.html)

3. Instale as dependências do arquivo `requirements.txt` com o comando

        pip install -r requirements.txt

4. Rode as migrations do Django com os comandos abaixo


        python manage.py makemigrations
        python manage.py migrate

5. Inicie o servidor Django com o comando

        python manage.py runserver

6. Abra o navegador em [http://localhost:8000/](http://localhost:8000/)


## Rodando a aplicação Flask

1. Entre na pasta `flask`

2. Crie e ative um [ambiente virtual com venv](https://docs.python.org/3/library/venv.html)

3. Instale as dependências do arquivo `requirements.txt` com o comando

        pip install -r requirements.txt

4. Inicie o servidor com o comando

        python app.py

5. Abra o navegador em [http://localhost:5000](http://localhost:5000)
