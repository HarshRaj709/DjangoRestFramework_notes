from django.db import models
class Products(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    def __str__(self):
        return self.title