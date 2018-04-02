from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.product_name
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Command(models.Model):
    cmd = models.ForeignKey(Product, on_delete=models.CASCADE)
    cmd_date = models.DateTimeField('date command')
    qte = models.IntegerField(default=0)

    def __str__(self):
        return self.cmd_date
