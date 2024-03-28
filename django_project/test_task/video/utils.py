import os.path
from uuid import uuid4

import cv2
import numpy
from django.http import HttpResponse, Http404
from pytils.translit import slugify

from test_task import settings
from video.models import VideoFile


def get_slug(text):
    slug = slugify(text)
    while VideoFile.objects.filter(slug=slug).exists():
        slug = f"{slug}-{uuid4().hex[:4]}"
    return slug


def create_video_opencv(text: str, slug: str):
    width, height = 100, 100
    video_length = 3
    fps = 60
    filename = f"{slug}.mp4"
    out = cv2.VideoWriter(
        os.path.join(settings.MEDIA_ROOT, filename),
        cv2.VideoWriter_fourcc(*"mp4v"),  # *"mp4v"  *"XVID" *'H264'
        fps,
        (width, height),
    )

    # Фон(черный)
    frame = numpy.zeros((height, width, 3), dtype=numpy.uint8)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 2
    font_thickness = 2
    font_color = (255, 255, 255)

    # Начальные координаты текста
    x = width
    y = (height + 20 * font_scale) // 2

    # Шаг перемещения текста
    dx = (width + len(text) * 20 * font_scale) // (video_length * fps)

    # Если последний символ не проходит пол экрана, округляем в большую сторону
    if (width + len(text) * 20 * font_scale) % (video_length * fps) > width // 2:
        dx += 1

    for _ in range(video_length * fps):
        frame.fill(0)
        x -= dx
        cv2.putText(frame, text, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)
    out.release()
    return filename


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
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as video:
            response = HttpResponse(video.read(), content_type="video")
            response["Content-Disposition"] = 'attachment; filename="%s"' % filename
            return response
    raise Http404
