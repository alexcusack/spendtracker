from django.urls import path

from . import ping
from .processemail import post_handler

urlpatterns = [
    path('ping/', ping.ping),
    path('postping/', ping.postPing),
    path('process/', post_handler),
]
