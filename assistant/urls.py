from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),
    path("api/chat/", views.chat_api, name="chat_api"),
]