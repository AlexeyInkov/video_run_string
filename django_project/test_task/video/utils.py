import os.path

import cv2
import numpy
from django.conf import settings

from uuid import uuid4
from pytils.translit import slugify


def get_slug(text):
    slug = slugify(text)
    while os.path.exists(os.path.join(settings.MEDIA_ROOT, f"{slug}.mp4")):
        slug = f'{slug}-{uuid4().hex[:4]}'
    return slug


def create_video_opencv(text: str):
    width, height = 100, 100
    video_length = 3
    fps = 60
    filename = f"{get_slug(text)}.mp4"
    out = cv2.VideoWriter(
        os.path.join(settings.MEDIA_ROOT, filename), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
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
