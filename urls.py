# chat_app/urls.py
from django.urls import path
from .views import MessageViewSet, SendMessageView

urlpatterns = [
    path('messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message-list'),
    path('send/', SendMessageView.as_view(), name='send-message'),
]
