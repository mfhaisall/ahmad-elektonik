from django.db import models

# Create your models here.
class ProdukBaru(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProdukUnggulan(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class SemuaProduk(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

