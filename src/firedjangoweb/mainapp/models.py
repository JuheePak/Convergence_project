from django.db import models
from embed_video.fields import EmbedVideoField


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video = EmbedVideoField()

