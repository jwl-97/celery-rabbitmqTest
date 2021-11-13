import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app = Celery('mysite',
             broker='amqp://canna:canna1234@localhost/canna_host',
             backend='rpc://',
             include=['mysite.core.tasks'])

app.config_from_object('django.conf', namespace='CELERY')  # change here
app.autodiscover_tasks()
