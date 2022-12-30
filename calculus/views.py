from django.shortcuts import render
from .serializers import ProductPaymentSerializer , ProductPaymentGetSerializer
from rest_framework.generics import CreateAPIView,RetrieveAPIView, ListAPIView
from django.http import JsonResponse
from .models import ProductPayment
from rest_framework.permissions import IsAuthenticated


#create , delete or update payment
class PaymentAPIView(CreateAPIView):
    serializer_class = ProductPaymentSerializer
    premission_class = [IsAuthenticated]
    def create(self, request):

        data = request.data
       
        _mutable = data._mutable

        data._mutable = True
        
        data['buyer'] = request.user
        
        data._mutable = _mutable

        print(data)
        serializer = self.serializer_class(data = data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return JsonResponse(serializer.data)

#clearing payment
class ClearingPayment():
    pass


class MyCalcView(RetrieveAPIView):

    serializer_class = ProductPaymentGetSerializer

    def get_queryset(self,buyer):

        qs1 = ProductPayment.objects.filter(buyer = buyer) 
        qs2 = ProductPayment.objects.filter(for_who = buyer)
        return (qs1 | qs2).distinct()

    def get(self, request):

        buyer = request.user

        qs = self.get_queryset(buyer)

        serializer = self.serializer_class(qs , many=True)

        return JsonResponse(serializer.data , safe=False)


