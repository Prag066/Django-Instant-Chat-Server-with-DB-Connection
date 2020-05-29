import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Person,Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.other_user = self.scope['url_route']['kwargs']['user_name']
        self.me = self.scope['user']
        my_chat_room = await self.person_obj_id(me=self.me,other=self.other_user)
        room_name = my_chat_room
        print('room Id',room_name)
        self.room_group_name = 'chat_%s'% room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    @database_sync_to_async
    def person_obj_id(self, me, other):
        p = Person.objects.get_or_new(me, other)
        return p[0]

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        uname = data['uname']
        self.create_chat_message = await self.create_my_message(uname=self.me, message=message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'uname':uname
            }
        )

    # Receive message from room group
    async def chat_message(self,event):
        message = event['message']
        uname = event['uname']
        await self.send(text_data=json.dumps({
            'message':message,
            'uname' : uname
        }))
    @database_sync_to_async
    def create_my_message(self,uname,message):
        o1 = User.objects.get(username=self.me)
        o2 = User.objects.get(username=self.other_user)
        my_msg = Person.objects.get_or_new(me=o1,other=o2)[0]
        print('ob', my_msg)
        e = Message.objects.create(user=uname, message=message, person=my_msg)
        return print('msg created',e)
