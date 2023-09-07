
# from channels.consumer import SyncConsumer, AsyncConsumer
# from channels.exceptions import StopConsumer
# import json
# from time import sleep
# import asyncio

from channels.consumer import SyncConsumer, AsyncConsumer

class ServiceConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("websocket connected..", event)
        await self.send({
            'type':'websocket_acepted'
        })    

# class ServiceConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("websocket connected...", event)
#         await self.send({
#             'type':'websocket.accept'
#         })
       
#     async def websocket_receive(self, event):
#         print("Message recieved...", event)
#         print("Message text...", event['text'])
#         for i in range(50):
#             await self.send({     
#                 'type':'websocket.send',
#                 'text': str(i)
#             })
#             await asyncio.sleep(0.5)
    
#     async def websocket_disconnect(self, event):
#         print("websocket disconnected...", event)
#         raise StopConsumer()
    
    # async def send_data(self, event):
    #     data = event['data']
    #     await self.send(text_data=data)

        

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join a specific group
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming messages
        pass

    async def send_message(self, event):
        # Send a message to the client
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
