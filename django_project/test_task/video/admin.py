from django.contrib import admin

from video.models import VideoFile


# Register your models here.
@admin.register(VideoFile)
class VideoFileAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "run_string",
        "file",
        "created_at",
    )
