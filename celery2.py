from celery import Celery
from celery.schedules import crontab

app = Celery('mymodule',
             broker='amqp://',
             backend='amqp://',
             include=['mymodule.tasks'])

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'update_data-every-single-minute': {
        'task': 'data.tasks.update_data',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}    


if __name__ == '__main__':
    app.start()