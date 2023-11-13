from django.shortcuts import render

# Create your views here.
# chat_app/views.py
# chat_app/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
from .forms import MessageForm

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        form = MessageForm(request.data)
        if form.is_valid():
            form.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

from django.views import View
from .forms import MessageForm

class SendMessageView(View):
    template_name = 'chat_app/send_message.html'

    def get(self, request, *args, **kwargs):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})