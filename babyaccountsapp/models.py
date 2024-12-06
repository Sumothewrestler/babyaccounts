# models.py
from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Mode(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ledger(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Head(models.Model):
    name = models.CharField(max_length=255, default='Default Head')  # Set a default value

    def __str__(self):
        return self.name

    
class Accounting(models.Model):
    GST_CHOICES = [
        ('with_gst', 'With GST'),
        ('without_gst', 'Without GST'),
    ]

    date = models.DateField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE, default=1)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=1)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, default=1)
    head = models.ForeignKey(Head, on_delete=models.CASCADE, default=1)
    cr = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    dr = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    gst = models.CharField(max_length=20, choices=GST_CHOICES, default='with_gst')
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.business.name} - {self.ledger.name} - CR: {self.cr}, DR: {self.dr}"