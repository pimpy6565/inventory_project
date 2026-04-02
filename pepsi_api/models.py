from django.db import models
from django.contrib.auth.models import User

class Flavor(models.Model):
    name = models.CharField(max_length = 64)
    posting_number = models.IntegerField()
    units = models.IntegerField()
    
    def __str__(self):
        return self.name
        
