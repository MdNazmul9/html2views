from django.db import models
import datetime
from django.conf import settings

# Create your models here.
class SendingInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=18, decimal_places=2)
    # Rname = models.CharField(max_length=255)
    # RPhone = models.CharField(max_length=32)
    # #Rphoto = models.ImageField()
    # RCIN = models.IntegerField()
    # RAddress = models.TextField()
    # RCountry = models.CharField(max_length=255)
    # Rgender = models.CharField(max_length=32)
    # ShopkeeperName = models.CharField(max_length = 255)
    # # ShopkeeperCIN = models.IntegerField()
    # #CommissionGivingAmt = models.DecimalField(max_digits=16, decimal_places=4)
    
    # CommissionGivingAmt = models.IntegerField()
    # #TotalSalesAmt = models.DecimalField(max_digits=16, decimal_places=2)
    # TotalSalesAmt = models.IntegerField()
    # # ContactEmail = models.EmailField()
    # ContactEmail = models.CharField(max_length=1000)
    # ProductDetails = models.TextField()
    # #user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Date = models.DateTimeField(auto_now=True)
    # Status = models.BooleanField(default=False)
    # TransactionStatus = models.BooleanField(default=False)

    
    # def __init__(self):
    #     return self.CommissionGivingAmt   
