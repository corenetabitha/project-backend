from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from store.models import Order, ReturnRequest
from store.serializers import OrderSerializer, ReturnRequestSerializer
from django.apps import AppConfig

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
