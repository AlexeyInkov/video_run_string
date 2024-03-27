import os


from django.http import HttpRequest, HttpResponse, Http404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView

from test_task import settings
from video.models import VideoFile
from video.utils import create_video_opencv, get_slug


def create_file(run_string: str) -> HttpResponse:
    video = VideoFile.objects.filter(run_string=run_string)
    if video.exists():
        filename = video.first().file
        filename = str(filename)
    else:
        slug = get_slug(run_string)
        video = VideoFile.objects.create(slug=slug, run_string=run_string)
        filename = create_video_opencv(run_string, slug)
        video.file = filename
        video.save()
    filepath = os.path.join(settings.MEDIA_URL, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as video:
            response = HttpResponse(video.read(), content_type="video")
            response["Content-Disposition"] = 'attachment; filename="%s"' % filename
            return response
    raise Http404


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
    success_url = reverse_lazy("video:list_video")

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
