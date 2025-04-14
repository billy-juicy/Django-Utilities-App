from celery import Celery

app = Celery('practice', broker='redis://localhost//', backend='redis://localhost/')

@app.task(name='practice.tasks.add_numbers')
def add_numbers(x, y):
    return x + y