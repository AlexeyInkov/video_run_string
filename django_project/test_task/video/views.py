import os

from django.conf import settings
from django.http import HttpRequest, HttpResponse, Http404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView

from video.models import VideoFile
from video.utils import create_video_opencv


# Create your views here.


def video_run_string(request: HttpRequest) -> HttpResponse:
    text = request.GET.get("text", "")
    filename = create_video_opencv(text)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as video:
            response = HttpResponse(video.read(), content_type="video")
            response["Content-Disposition"] = 'attachment; filename="%s"' % filename
            return response
    raise Http404


class VideoListView(ListView):
    queryset = VideoFile.objects.all().order_by("-create_at")


class VideoCreateView(CreateView):
    model = VideoFile
    fields = ["run_string"]


class VideoDetailView(DetailView):
    model = VideoFile


class VideoDeleteView(DeleteView):
    model = VideoFile
    success_url = reverse_lazy("author_list")
