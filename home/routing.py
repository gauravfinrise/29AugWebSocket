# from django.urls import path
# # from home.consumers import *
# # from channels import consumer
# from .import consumers

# websocket_urlpatter = [
#     path("ws/sc/", consumers.MySyncConsumer.as_asgi()),
#     path("ws/ac/", consumers.MyAsyncConsumer.as_asgi()),
# ]


from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import consumers
from myapp.consumers import *

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        [
            path("ws/sc/", consumers.MySyncConsumer.as_asgi()),
            path("ws/ac/", consumers.MyAsyncConsumer.as_asgi()),
            path("ws/msc/", ServiceConsumer.as_asgi()),

            #Add more URL patterns for different consumers if needed
        ]
    ),
})