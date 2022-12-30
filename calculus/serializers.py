
from rest_framework import serailizers 
from .models import ProductPayment

class ProductPaymentSerializer(serailizers.ModelSerializer):
    
    class Meta:
        model = ProductPayment
        fields = '__all__'