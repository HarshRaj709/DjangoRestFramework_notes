from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Songs(models.Model):
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')             #many-to-one
    title = models.CharField(max_length=50)
    Musician = models.CharField(max_length=50)

    def __str__(self):
        return self.title
