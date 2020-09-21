import datetime
from django.db import models

# Create your models here.


class tools(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    Details = models.URLField(max_length=500)
    Buy = models.URLField(max_length=500)
    Types = models.CharField(max_length=50)
    Video = models.URLField(max_length=500)

    def __str__(self):
        return  self.name


class contact(models.Model):

    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    email = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True , blank=True) 

    def __str__(self):
        return 'Message from ' + self.name


class Handtool1(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    Details = models.URLField(max_length=500)
    Buy = models.URLField(max_length=500)
    Video = models.URLField(max_length=500)

    def __str__(self):
        return  self.name



class Powertool1(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    Details = models.URLField(max_length=500)
    Buy = models.URLField(max_length=500)
    Video = models.URLField(max_length=500)

    def __str__(self):
        return  self.name


class Measuringtool1(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    Details = models.URLField(max_length=500)
    Buy = models.URLField(max_length=500)
    Video = models.URLField(max_length=500)

    def __str__(self):
        return  self.name



class Machinetool1(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    Details = models.URLField(max_length=500)
    Buy = models.URLField(max_length=500)
    Video = models.URLField(max_length=500)

    def __str__(self):
        return  self.name



class Automotivetool1(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    Details = models.URLField(max_length=500)
    Buy = models.URLField(max_length=500)
    Video = models.URLField(max_length=500)

    def __str__(self):
        return  self.name