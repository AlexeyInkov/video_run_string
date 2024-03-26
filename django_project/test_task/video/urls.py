from django.urls import path

from .views import (
    video_run_string,
    VideoListView,
    VideoCreateView,
    VideoDetailView,
    VideoDeleteView,
)

app_name = "video"

urlpatterns = [
    path("/", VideoListView.as_view(), name="list_video"),
    path("add/", video_run_string, name="add_video"),
    path("create/", VideoCreateView.as_view(), name="create_video"),
    path("<slug:slug>/", VideoDetailView.as_view(), name="detail_video"),
    path("<slug:slug>/delete/", VideoDeleteView.as_view(), name="delete_video"),
]
