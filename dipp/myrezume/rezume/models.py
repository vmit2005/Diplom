from django.db import models

class Rezume(models.Model):
    title = models.CharField(max_length=100)
    date1 = models.CharField(max_length=20)
    date2 = models.CharField(max_length=20,blank=True)
    description = models.CharField(max_length=250)

class Acad(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='rezume/media/')
    url= models.URLField(blank=True)
