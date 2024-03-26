
from django.urls import path

from .views import video_run_string


app_name = "video"


urlpatterns = [
    path("add/", video_run_string, name="create_video"),
]
