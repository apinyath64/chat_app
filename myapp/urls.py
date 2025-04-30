from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room),
    path('<str:room>/<str:username>/', views.message, name='room'),
]
