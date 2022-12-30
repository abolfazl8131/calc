
from django.urls import path
from .views import PaymentAPIView,MyCalcView

urlpatterns = [
    path('new/' , PaymentAPIView.as_view()),
    path('all/' ,MyCalcView.as_view())
]
