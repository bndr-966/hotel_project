from django.db import models

# Create your models here.
class manu(models.Model):
    food=models.CharField(max_length=50)
    drink=models.CharField(max_length=50)
    