from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class CurrencyData(models.Model):
    code = models.CharField(max_length=10)
    value = models.FloatField()