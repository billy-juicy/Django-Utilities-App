from celery import shared_task
from billing.models import Debt

@shared_task
def update_debt():
    for debt in Debt.objects.all():
        # debt.save()
        print('hello')