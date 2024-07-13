from django.db import models

class Profile(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField(max_length=10)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    

class Episode(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    directed_by = models.CharField(max_length=255)
    written_by = models.CharField(max_length=255)
    storyboarded_by = models.CharField(max_length=255)
    original_air_date = models.DateField(max_length=10)
    summary = models.TextField(max_length=2000)