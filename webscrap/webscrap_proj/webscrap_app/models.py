from django.db import models

# Create your models here.
class Links(models.Model):
    address=models.CharField(max_length=500,null=True,blank=True)
    string=models.CharField(max_length=500,null=True,blank=True)