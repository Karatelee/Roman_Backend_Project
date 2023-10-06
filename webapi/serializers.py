from .models import Dish, Order, OrderDish
from rest_framework import serializers

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class OrderDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDish
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    dishes = OrderDishSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'