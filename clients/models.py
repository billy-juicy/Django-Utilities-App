from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    last_name = models.CharField(max_length=100) # Фамилия
    first_name = models.CharField(max_length=100) # Имя
    middle_name = models.CharField(max_length=100, blank=True, null=True) # Отчество с необязательным заполнением
    phone = models.CharField(max_length=20) # Телефон
    address = models.TextField() # Адрес
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE) # Внешний ключ к таблице Пользователь

    class Meta:
        verbose_name_plural = "Clients"
        verbose_name = "Client"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

