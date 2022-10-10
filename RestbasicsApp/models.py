import json
from typing import List
from django.db import models

class CarModel(models.Model):
    Make_ID = models.IntegerField()
    Make_Name = models.CharField(max_length= 100)
    Model_ID =  models.IntegerField()
    Model_Name = models.CharField(max_length= 100)

class Data(models.Model):
    Count = models.IntegerField()
    Message = models.CharField(max_length=200)
    SearchCriteria = models.CharField(max_length=200)
    Results = models.ManyToManyField(CarModel, blank=True)