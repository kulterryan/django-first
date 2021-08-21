from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    msg = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.email