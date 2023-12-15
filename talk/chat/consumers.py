from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .models import Message, ChatRoom
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.channel_layer,
            self.room_group_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room_slug = data['room_slug']

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room_slug': room_slug
            }
        )

        await self.save_message(username, room_slug, message)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room_slug = event['room_slug']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room_slug': room_slug
        }))
    
    @sync_to_async
    def save_message(self, username, room_slug, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room_slug)
        Message.objects.create(user=user, room=room, text=message)
