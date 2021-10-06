from django.db import models
from .drug_types import drug_types_list


class Drug(models.Model):
    drug_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50, unique=True)
    drug_type = models.CharField(max_length=20, choices=drug_types_list, default='pills')
    amount = models.CharField(max_length=20)
    exp = models.DateField(auto_now_add=True)
    mfg = models.DateField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    description = models.TextField() 
    updated_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
