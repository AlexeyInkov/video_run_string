# Видео с бегущей строкой

## Установка

#### Установка зависимостей

```pip install poetry```

```poetry install```

```python manage.py migrate```

```python manage.py createsuperuser```

#### Запуск

- локально ```python manage.py runserver ```

#### В браузере

* локально

  - admin панель    ```http://127.0.0.1:8000/admin```
  - создание видео  ```http://127.0.0.1:8000/video/add/?text="текст бегещей строки"```
  - создание видео  ```http://127.0.0.1:8000/video/create```
  - список видео    ```http://127.0.0.1:8000/video/```
  - просмотр видео  ```http://127.0.0.1:8000/video/<slug>```
  - удаление видео  ```http://127.0.0.1:8000/video/<slug>/delete/```
