from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=500)
    release_year = models.IntegerField(blank=True, null=True)
    platforms = models.TextField(blank=True, null=True)
    steam_link = models.URLField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    rating_max = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.title
