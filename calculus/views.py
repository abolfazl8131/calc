from django.shortcuts import render
from .serializers import ProductPaymentSerializer , ProductPaymentGetSerializer
from rest_framework.generics import CreateAPIView,RetrieveAPIView, ListAPIView,UpdateAPIView
from django.http import JsonResponse,HttpResponse
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


class MyCalcView(RetrieveAPIView):

    serializer_class = ProductPaymentGetSerializer
    premission_class = [IsAuthenticated]
    def get_queryset(self,buyer):

        qs1 = ProductPayment.objects.filter(buyer = buyer) 
        qs2 = ProductPayment.objects.filter(for_who = buyer)
        return (qs1 | qs2).distinct()

    def get(self, request):

        buyer = request.user

        qs = self.get_queryset(buyer)

        serializer = self.serializer_class(qs , many=True)

        return JsonResponse(serializer.data , safe=False)


from logic.payment_logic import payment_report

class MyCalcReport(RetrieveAPIView):

    premission_class = [IsAuthenticated]
    def get_queryset(self,buyer):

        qs1 = ProductPayment.objects.filter(buyer = buyer ,is_done=False) 
        qs2 = ProductPayment.objects.filter(for_who = buyer,is_done=False)
        return (qs1 | qs2).distinct()

    def get(self, request):

        user = request.user

        qs = self.get_queryset(user)
        
        reports = payment_report(user,qs,self.get_queryset)

        return JsonResponse({"reports":reports})

#clearing payment
class ClearingPayment(UpdateAPIView):

    premission_class = [IsAuthenticated]

    def get_object(self , **kwargs):
        try:
            obj = ProductPayment.objects.get(is_done= False , **kwargs)
            return obj
        except:
            raise 'you cant update this object'

    def patch(self, request):

        user = request.user

        id = request.GET.get('id')

        obj = self.get_object(for_who = user , id = id)

        obj.done()


        return JsonResponse({'status':'done'})




