from django.db import models

# Create your models here.

class List_Item(models.Model):
    label = models.CharField((""), max_length=50),
    actif = models.BooleanField
