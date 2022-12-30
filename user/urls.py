
from django.urls import path
from .views import UserAPIView,ViewAllUsers
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
   path('register/' , UserAPIView.as_view()),
   path('all/' , ViewAllUsers.as_view()),
   path('auth/' , jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair')
]
