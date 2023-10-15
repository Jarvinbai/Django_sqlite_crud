from django.db import models

# Create your models here.

class people(models.Model):
    Name=models.CharField(max_length=20,default="")
    Mail=models.CharField(max_length=20,default="")
    password=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.Name



