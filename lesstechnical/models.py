from django.db import models

# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    created = models.DateTimeField("date created")
    published = models.DateTimeField("date published")
    picture = models.URLField
    author = models.CharField(max_length=30, default='Matt') 

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    less_tech_text = models.TextField
    more_tech_text = models.TextField

