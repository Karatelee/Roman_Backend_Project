from .serializers import DishSerializer, OrderSerializer
from rest_framework.response import Response
from .models import Dish, Order, OrderDish
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend



class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        'price': ['exact', 'lte', 'gte'],
    }
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwner, 
    # ]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        'id': ['exact'],
    }
    ordering_fields = ['id']
    
    def create(self, request, *args, **kwargs):
        dishes = request.data.pop('dishes')
        order = Order.objects.create(**request.data)
        for dish in dishes:
            order.dishes.add(OrderDish.objects.create(dish_id=dish['id'], quantity=dish['quantity']))
        order.save()
        return Response(OrderSerializer(order).data, status=201)



# class SpecialMenuForChildrenView(View):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse({'message': 'Special menu for children endpoint'})