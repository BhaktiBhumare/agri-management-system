from django.db import models
from crops.models import Crop

class Expense(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField()

class Income(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()

