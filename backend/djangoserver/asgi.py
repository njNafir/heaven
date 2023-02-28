"""
ASGI config for djangoserver project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns

django_asgi_app = get_asgi_application()

# the websocket will open at 127.0.0.1:8000/ws/<room_name>
application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    ,
})
