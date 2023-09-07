from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from channels.consumer import SyncConsumer, AsyncConsumer

class TestConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data = json.dumps({'status':'connected from django channels'}))

    def receive(self , text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status':'we go you'}))

    def disconnect(self, *args, **kwargs):
        # Called when the socket closes
        print('disconnected')       
        
    def send_notification(self, event):
        print('send_notifiaction')
        print(event)
        print('send_notification')


# class MySyncConsumer(SyncConsumer):
#     def websocket_connect(self):
#         print("websocket connected...")
    
#     def websocket_recieve(slef):
#         print("Message recieved...")
    
#     def websocket_disconnect(self):
#         print("websocket disconnected...")


# class MyAsyncConsumer(AsyncConsumer):
#     async def websocket_connect(self):
#         print("websocket connected...")
    
#     async def websocket_recieve(slef):
#         print("Message recieved...")
    
#     async def websocket_disconnect(self):
#         print("websocket disconnected...")
        