import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from martor.models import MartorField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    content = MartorField()

    draft = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class UserPost(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs={'slug': self.slug})
