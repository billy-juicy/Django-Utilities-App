import os
from celery import Celery

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice.settings')

app = Celery('practice', broker='redis://localhost//', backend='redis://localhost//')

# Используем строку для автоматического обнаружения задач из всех зарегистрированных приложений Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоподгрузка задач из всех зарегистрированных приложений Django
app.autodiscover_tasks()