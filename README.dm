-- Параметры базы данных PostgreSQL, которая должна быть создана заранее
PostgreSQL:
    dataBase="postgres
    table="test_table"
    user="postgres",
    password="123",

-- необходимо установить следующие пакеты:

sudo apt upgrade
sudo apt update

sudo apt install libpq-dev

pip install google-auth google-auth-httplib2 google-api-python-client --upgrade
pip install psycopg2-binary
pip install psycopg2



sudo apt -y install postgresql
    sudo -u postgres psql
        \password postgres # Необходимо установить пароль "123"


sudo apt install celery
pip install Celery

необходимо открыть 2 терминала
    1) в первом запустить сервис Redis:
        
        redis-server
    
    
    2) во первом запустить сервис Celery:
        
        celery -A tasks worker -B --loglevel=DEBUG