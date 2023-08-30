from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from your_app import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/<str:ticket_id>/', consumers.ChatConsumer.as_asgi()),
    ]),
})
