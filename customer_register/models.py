from django.db import models

# Create your models here.

class Area(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    previous_address = models.CharField(max_length=100)
    telephone_number= models.CharField(max_length=15)
    area= models.ForeignKey(Area,on_delete=models.CASCADE)
