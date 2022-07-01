-- необходимо установить следующие пакеты:

sudo apt install libpq-dev
sudo apt install celery

sudo apt -y install postgresql
    sudo -u postgres psql
        \password postgres # Необходимо установить пароль "123"

-- Параметры базы данных PostgreSQL, которая должна быть создана заранее
PostgreSQL:
    dataBase="postgres
    table="test_table"
    user="postgres",
    password="123",


pip install google-auth google-auth-httplib2 google-api-python-client --upgrade
pip install psycopg2-binary
pip install psycopg2
pip install Celery


необходимо открыть 2 терминала
    1) в первом запустить сервис Redis:
        
        redis-server
    
    
    2) во втором запустить сервис Celery:
        
        celery -A tasks worker -B --loglevel=DEBUG