from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='profile_picture.png', upload_to='profile_pictures')
    summary = models.TextField(max_length=200, blank=True)
    first_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=False, max_length=30)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'
