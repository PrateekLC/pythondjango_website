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

class contactus(models.Model):
    mainaddress= models.CharField(max_length=1000)
    streetaddress= models.CharField(max_length=1000)
    phonenumber= models.CharField(max_length=20)
    openinghrs= models.CharField(max_length=1000)
    email= models.EmailField()

    def __str__(self):
        return self.email

class ourpackage(models.Model):
    packagename=models.CharField(max_length=500)
    packdis=models.CharField(max_length=500)
    line1=models.TextField()
    line2=models.TextField()
    line3=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.packagename

class contactform(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank= True)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name