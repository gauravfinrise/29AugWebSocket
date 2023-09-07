# core/routing.py
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import consumers
from home.consumers import *
from myapp.consumers import *

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        [
            path("ws/service/", MyConsumer.as_asgi()),
            path("ws/test/", consumers.TestConsumer.as_asgi()),
            path("ws/sc/", MySyncConsumer.as_asgi()),
            path("ws/ac/", MyAsyncConsumer.as_asgi()),
            #Add more URL patterns for different consumers if needed
        ]
    ),
})



# from django.urls import path
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from .import consumers

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter(
#         path("ws/some_path/", consumers.SomeConsumer.as_asgi()),
#     ),
# })