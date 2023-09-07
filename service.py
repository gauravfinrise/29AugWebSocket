import asyncio
import websockets

# Maintain a list of connected clients
clients = []

async def service(websocket, path):
    clients.append(websocket)
    try:
        async for message in websocket:
            print(f"Service received: {message}")
            # Process the message and send a response to all connected clients
            response = f"Service processed: {message}"
            for client in clients:
                await client.send(response)
    finally:
        clients.remove(websocket)

start_server = websockets.serve(service, "localhost", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
