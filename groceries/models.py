from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)