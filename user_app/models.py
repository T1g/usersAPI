from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=50)
    age = models.IntegerField()
    voice_actors = models.CharField(max_length=255)
    summary = models.TextField(max_length=2000)
    
class Episode(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    directed_by = models.CharField(max_length=255)
    written_by = models.CharField(max_length=255)
    storyboarded_by = models.CharField(max_length=255)
    original_air_date = models.DateField(max_length=10)
    summary = models.TextField(max_length=2000)