# Sistema de processos UFBA

Sistema de gerenciamento de processos da UFBA.

-----

Comandos da aplicação:
``` shell
$ virtualenv -p python3 .env/         # cria o ambiente virtual
$ source .env/bin/activate            # ativa o ambiente virtual
$ pip install -r requirements.txt     # instala as dependências

$ python src/manage.py migrate --run-syncdb # aplica as migrações pro sqlite

$ python src/manage.py runserver       # inicia o servidor da aplicação
```
