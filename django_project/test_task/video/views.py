import os

from django.conf import settings
from django.http import HttpRequest, HttpResponse, FileResponse, Http404
from django.shortcuts import render

from video.utils import create_video_opencv


# Create your views here.


def video_run_string(request: HttpRequest) -> HttpResponse:
    text = request.GET.get('text', '')
    filename = create_video_opencv(text)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as video:
            response = FileResponse(video.read(), content_type="video")
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename
            return response
    raise Http404
