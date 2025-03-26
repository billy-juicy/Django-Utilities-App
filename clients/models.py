from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Clients"
        verbose_name = "Client"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"