from django.db import models

# Create your models here.


class Profile(models.Model):

    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    


    def __unicode__(self): 
        return (self.name)

    def __str__(self):
        return self.name 



class Social(models.Model):

    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)
    icon = models.CharField(max_length=100)

    def __unicode__(self): 
        return (self.name)