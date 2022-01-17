from django.db import models

# Create your models here.


class Fruits(models.Model) :  #     fruist(상속받을값)
    name = models.CharField(max_length=20)
    price = models.IntegerField()





