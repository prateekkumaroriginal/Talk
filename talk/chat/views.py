from django.shortcuts import render
from django.views import View
from .models import ChatRoom, Message

# Create your views here.
class IndexView(View):
    def get(self, request):
        rooms = ChatRoom.objects.all()
        return render(request, 'chat/index.html', {'rooms':rooms})

class ChatRoomView(View):
    def get(self, request, slug):
        room = ChatRoom.objects.get(slug=slug)
        messages = Message.objects.filter(room=room)
        return render(request, 'chat/chatroom.html', {'room':room, 'messages': messages})
        