from django.db import models


class VideoFile(models.Model):
    run_string = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    file = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
