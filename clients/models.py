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

class Complaint(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_filed = models.DateField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=50,
                              choices=[("open", "Open"), ("in progress", "In Progress"), ("resolved", "Resolved")])

    class Meta:
        verbose_name_plural = "Complaints"
        verbose_name = "Complaint"

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name}"

class Property(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.TextField()
    type = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Properties"
        verbose_name = "Property"

    def __str__(self):
        return f"{self.owner.first_name} {self.owner.last_name}"