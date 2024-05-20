from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Customer, Purchase
from .serializers import CustomerSerializer, PurchaseSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['get'], url_path='score', url_name='score')
    def score(self, request, pk=None):
        customer = self.get_object()
        return Response({'id': customer.id, 'loyalty_score': customer.loyalty_score})

    @action(detail=True, methods=['get'], url_path='purchases', url_name='purchases')
    def purchases(self, request, pk=None):
        customer = self.get_object()
        purchases = Purchase.objects.filter(customer=customer)
        page = self.paginate_queryset(purchases)
        if page is not None:
            serializer = PurchaseSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)
