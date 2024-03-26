
from django.urls import path

from .views import VideoRunStringView


app_name = "video"


urlpatterns = [
    path("add/", VideoRunStringView.as_view(), name="create_video"),
]