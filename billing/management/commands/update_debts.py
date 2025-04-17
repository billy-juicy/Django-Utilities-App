from django.core.management.base import BaseCommand
from billing.models import Debt

class Command(BaseCommand):
    help = 'Обновляет все записи в Debt'

    def handle(self, *args, **options):
        updated_count = 0
        for debt in Debt.objects.all():
            debt.save()
            updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Успешно обновлено {updated_count} записей Debt')
        )