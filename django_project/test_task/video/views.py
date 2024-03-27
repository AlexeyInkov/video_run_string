from django.http import HttpRequest, HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from video.models import VideoFile
from video.utils import create_file


def video_run_string(request: HttpRequest) -> HttpResponse:
    run_string = request.GET.get("text", None)
    if run_string is None:
        raise Http404
    return create_file(run_string)


class VideoListView(ListView):
    queryset = VideoFile.objects.all().order_by("-created_at")


class VideoCreateView(CreateView):
    model = VideoFile
    fields = ["run_string"]

    def post(self, request, *args, **kwargs):
        run_string = request.POST.get("run_string", None)
        if run_string is None:
            raise Http404
        return create_file(run_string)


class VideoDetailView(DetailView):
    model = VideoFile


class VideoDeleteView(DeleteView):
    model = VideoFile
    success_url = reverse_lazy("video:list_video")
