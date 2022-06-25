from django.db import models

# Create your models here.
class Fruits(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    price=models.IntegerField()