from django.db import models

class Rezume(models.Model):
    title = models.CharField(max_length=100)
    date1 = models.CharField(max_length=20)
    date2 = models.CharField(max_length=20,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Acad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='rezume/media/')
    url= models.URLField(blank=True)

    def __str__(self):
        return self.title

class Arbeit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    drawing = models.FileField(upload_to='arbeit/media/',blank=True)
    dr_spec = models.FileField(upload_to='arbeit/media/', blank=True)
    dr_model = models.FileField(upload_to='arbeit/media/', blank=True)


    def __str__(self):
        return self.title


class Proggg(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.URLField(blank=True)



    def __str__(self):
        return self.title

