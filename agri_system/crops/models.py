from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    sowing_date = models.DateField()
    harvest_date = models.DateField()

    def __str__(self):
        return self.crop_name

