
from django.urls import path
from .views import PaymentAPIView,MyCalcView,MyCalcReport

urlpatterns = [
    path('new/' , PaymentAPIView.as_view()),
    path('all/' ,MyCalcView.as_view()),
    path('report/' , MyCalcReport.as_view())
]
