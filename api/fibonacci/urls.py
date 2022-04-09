from django.urls import path
from .views import *

urlpatterns = [
    path('fibonacci/eval/', FibonacciValue.as_view())
]
