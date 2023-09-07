
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
import json
from time import sleep
import asyncio
  
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("websocket connected...", event)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        # event=json.dumps({'status':'we go you'})
        print("Message recieved...", event)
        print("Message text...", event['text'])
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text': str(i)
            })
            sleep(0.5)
    
    def websocket_disconnect(self, event):
        print("websocket disconnected...",)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket connected...", event)
        await self.send({
            'type':'websocket.accept'
        })
       
    async def websocket_receive(self, event):
        print("Message recieved...", event)
        print("Message text...", event['text'])
        for i in range(50):
            await self.send({     
                'type':'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(0.5)
    
    async def websocket_disconnect(self, event):
        print("websocket disconnected...", event)
        raise StopConsumer()
        