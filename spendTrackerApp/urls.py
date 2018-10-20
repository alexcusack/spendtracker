from django.urls import path

from . import ping
from .processemail import post_handler
from .chat import handle_message

urlpatterns = [
    path('ping/', ping.ping),
    path('postping/', ping.postPing),
    path('process/', post_handler),
    path('chat/', handle_message)
]
