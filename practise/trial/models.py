from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    subject = models.CharField(max_length=50)