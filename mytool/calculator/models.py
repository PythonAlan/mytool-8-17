from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Rate_Info(models.Model):
    first_class_us = models.FloatField()
    first_class_uk = models.FloatField()
    first_class_de = models.FloatField()
    first_class_au = models.FloatField() #以上为头程

    second_class_us = models.FloatField()
    second_class_uk = models.FloatField()
    second_class_de = models.FloatField()
    second_class_au = models.FloatField()


    gz_us = models.FloatField()
    gz_uk = models.FloatField()
    gz_de = models.FloatField()
    gz_au = models.FloatField()


    exchange_rate_us = models.FloatField()
    exchange_rate_uk = models.FloatField()
    exchange_rate_de = models.FloatField()
    exchange_rate_au = models.FloatField()

    commission_rate = models.FloatField()

