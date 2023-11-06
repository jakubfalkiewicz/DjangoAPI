from django.db import models

# Create your models here.

class CurrencyData(models.Model):
    code = models.CharField(max_length=10)
    value = models.FloatField()