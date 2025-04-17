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
    date_issued = models.DateField(db_index=True)
    due_date = models.DateField(db_index=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Invoices"
        verbose_name = "Invoice"

    def __str__(self):
        return f"{self.client} {self.date_issued}"

class Tariff(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Tariffs"
        verbose_name = "Tariff"

    def __str__(self):
        return f"{self.service} {self.rate}"

class Debt(models.Model):
    UNPAID = 'unpaid'
    PAID = 'paid'
    OVERDUE = 'overdue'
    CHOICES_STATUS = [
        (UNPAID, 'unpaid'),
        (PAID, 'unpaid'),
        (OVERDUE, 'overdue'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(db_index=True)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, default=UNPAID)

    class Meta:
        verbose_name_plural = "Debts"
        verbose_name = "Debt"

    def __str__(self):
        return f"{self.client} {self.amount}"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    date_paid = models.DateField(db_index=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Payments"
        verbose_name = "Payment"

    def __str__(self):
        return f"{self.invoice} {self.date_paid}"

class Meter(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    meter_number = models.CharField(max_length=50)
    installation_date = models.DateField(db_index=True)

    class Meta:
        verbose_name_plural = "Meters"
        verbose_name = "Meter"

    def __str__(self):
        return f"{self.client} {self.service} {self.meter_number}"

class MeterReading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    reading_date = models.DateField(db_index=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "MeterReadings"
        verbose_name = "MeterReading"

    def __str__(self):
        return f"{self.meter} {self.reading_date}"