from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:room>/', ChatConsumer.as_asgi()),
]