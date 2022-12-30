from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveAPIView, ListAPIView
from .serializers import UserSerializer
from django.http import JsonResponse
from .models import User

# Create your views here.

class UserAPIView(CreateAPIView):

    serializer_class = UserSerializer

    def create(self,request):

        data = request.data

        serializer = self.serializer_class(data = data)

        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return JsonResponse({'username':serializer.data['username']} , status = 200)
    

class ViewAllUsers(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    