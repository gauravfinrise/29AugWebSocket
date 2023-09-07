# websocket_utils.py

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

async def send_message_to_group(room_name, message):
    await channel_layer.group_send(
        f"chat_{room_name}",
        {
            "type": "send_message",
            "message": message
        }
    )
