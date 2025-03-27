from django.db import models
from clients.models import Client

class Service(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"

    def __str__(self):
        return f"{self.name} {self.unit}"

class Invoice(models.Model):
    client = models.ForeignKey(Client, db_index=True, on_delete=models.CASCADE)
    date_issued = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Invoices"
        verbose_name = "Invoice"

    def __str__(self):
        return f"{self.client} {self.date_issued}"
