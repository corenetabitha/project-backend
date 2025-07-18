from rest_framework import serializers
from .models import Order, ReturnRequest

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
python manage.py makemigrations store
python manage.py migrate


class ReturnRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnRequest
        fields = '__all__'
