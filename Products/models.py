from django.db import models
from datetime import datetime
import requests

# Create your models here.
class Machine(models.Model):
    machineName = models.CharField(max_length=50)
    machinePrice = models.IntegerField(blank= False)
    machineDescription = models.CharField(max_length=50000)
    machineNegotiatable= models.BooleanField(default= False)
    machineImage= models.ImageField(null= False, blank= False, upload_to= 'images/')
    user = models.CharField(max_length=1000, default='admin')
    dt = models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        name= self.machineName
        price= self.machinePrice
        user = self.user
        return f'{name}..[{price}] {user}'
