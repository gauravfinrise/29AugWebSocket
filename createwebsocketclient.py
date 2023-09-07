import asyncio
import json
websockets = __import__('websockets')

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Connect to a WebSocket server and send/receive messages'

    async def handle(self, *args, **kwargs):
        # WebSocket server URL
        websocket_uri = "ws://localhost:8000/some_path/your_room_name/"

        async with websockets.connect(websocket_uri) as websocket:
            while True:
                message = input("Enter a message to send (or 'q' to quit): ")
                if message == 'q':
                    break

                await websocket.send(json.dumps({"message": message}))
                response = await websocket.recv()

                data = json.loads(response)
                received_message = data.get("message")

                self.stdout.write(self.style.SUCCESS(f"Received message: {received_message}"))

