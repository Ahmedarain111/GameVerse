from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    liked_games = models.ManyToManyField('games.Game', related_name='liked_by', blank=True)
    wishlist = models.ManyToManyField('games.Game',     related_name='wishlisted_by', blank=True)
    played_games = models.ManyToManyField('games.Game', related_name='played_by', blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email
    
