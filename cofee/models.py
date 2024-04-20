from django.db import models

# Create your models here.
class cofee(models.Model):
    name = models.CharField(max_length=225)  # Fixed typo in max_length
    price = models.FloatField()
    quantity = models.IntegerField()  # Changed field name to lowercase, following convention
    image = models.CharField(max_length=2083)
    
