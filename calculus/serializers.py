
from rest_framework import serializers
from .models import ProductPayment
from user.models import User
from user.serializers import UserSerializer
class ProductPaymentSerializer(serializers.ModelSerializer):
    buyer = serializers.SlugRelatedField(queryset = User.objects.all() , slug_field='username')
    class Meta:
        model = ProductPayment
        fields = '__all__'

        extra_kwargs = {'buyer': {'read_only': True}}





class ProductPaymentGetSerializer(serializers.ModelSerializer):
    buyer = UserSerializer()
    for_who = UserSerializer()

    class Meta:
        model = ProductPayment
        fields = '__all__'
      
       