from django.db import models
import datetime

# Create your models here.
class SendingInfo(models.Model):
    name = models.CharField(max_length=255)
    contact  = models.EmailField(max_length=64)
    content = models.TextField()

    def __str__(self):
        return self.name

