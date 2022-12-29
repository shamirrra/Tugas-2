from django.db import models

class WatchList(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.CharField(max_length=200)