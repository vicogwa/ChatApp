from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers  



from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})