from django.db import models
from datetime import datetime
# import request

# Create your models here.
class MachineCategory(models.Model):
    name = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name
    
class MachineBrand(models.Model):
    name = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name
    
class Machine(models.Model):
    machineName = models.CharField(max_length=50)
    machinePrice = models.DecimalField(default= 0, decimal_places= 2, max_digits= 9, null= False, blank= False)
    machineDescription = models.CharField(max_length=50000)
    machineNegotiatable= models.BooleanField(default= False)
    machineImage= models.ImageField(null= False, blank= False, upload_to= 'images/')
    machineCategory = models.ForeignKey(MachineCategory, on_delete= models.CASCADE, default= 1)
    machineBrand = models.ForeignKey(MachineBrand, on_delete= models.CASCADE, default= 1)
    is_sale = models.BooleanField(default= False)
    sale_price = models.DecimalField(default= 0, decimal_places= 2, max_digits= 6)
    user = models.CharField(max_length=1000, default='admin')
    dt = models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        name= self.machineName
        price= self.machinePrice
        user = self.user
        return f'{name}..[{price}] {user}'
    
class BrandImages(models.Model):
    brandName= models.ForeignKey(MachineBrand, on_delete= models.CASCADE, default= 1)
    brandImage= models.ImageField(null= False, blank= False, upload_to= 'brand/')

    def __str__(self):
        return f'{self.brandName}'

class Gender(models.Model):
    gender= models.CharField(max_length=10)

    def __str__(self):
        return f'{self.gender}'

class FeedBack(models.Model):
    customerName= models.CharField(max_length= 20)
    customerGender= models.ForeignKey(Gender, on_delete= models.CASCADE, default=1)
    customerMessage= models.TextField()

    def __str__(self):
        return f'{self.customerName}'



