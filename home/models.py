from django.db import models

# Create your models here.
class aboutme(models.Model):
    name = models.CharField(max_length=500)
    description=models.TextField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
class service(models.Model):
    name = models.CharField(max_length=500)
    description= models.TextField()
    logo = models.CharField(max_length=300)


    def __str__(self):
        return self.name

class feedback(models.Model):
    name= models.CharField(max_length=500)
    position= models.CharField(max_length=1000)
    comment=models.TextField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name