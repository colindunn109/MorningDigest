from django.db import models
import datetime

class Article(models.Model):
    title = models.CharField(max_length = 128,unique=True)
    summary = models.TextField(max_length = 128)
    content = models.TextField()
    url = models.URLField(max_length=280,default="",unique=True)
    thumbnail = models.ImageField(default="https://cdn3.iconfinder.com/data/icons/tech-icons/64/Computer_Chip-512.png")
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    ordering = ['timestamp']

    def __str__(self):
        return self.title

    '''
        We also want URL, for a link to relevant news info
        an image to represent the headline
        a user associated with this post
    '''

class PoliticsArticle(models.Model):
    title = models.CharField(max_length = 128,unique=True)
    summary = models.TextField(max_length = 128)
    content = models.TextField()
    url = models.URLField(max_length=280,default="",unique=True)
    thumbnail = models.ImageField(default = "https://miro.medium.com/max/800/1*bNfxs62uJzISTfuPlOzOWQ.png")

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length = 128)
    summary = models.TextField(max_length = 128)
    content = models.TextField()
