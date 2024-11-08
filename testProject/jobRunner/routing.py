from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/progress/", consumers.progressConsumer.as_asgi()),
]