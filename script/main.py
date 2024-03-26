import os
from sys import argv

import cv2
import numpy


def create_video_opencv(text: str):
    width, height = 100, 100
    video_length = 3
    fps = 60
    filename = "my_video.mp4"
    out = cv2.VideoWriter(
        filename,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
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
        cv2.putText(
            frame,
            text,
            (x, y),
            font,
            font_scale,
            font_color,
            font_thickness
            )
        out.write(frame)
    out.release()


def main():
    string = input('Введи текст: ')
    create_video_opencv(string)


if __name__ == '__main__':
    main()

