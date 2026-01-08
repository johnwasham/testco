from django.shortcuts import render

# from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer

def index(request):
    data = {
        'message': 'hello world',
    }

    return JsonResponse(data)

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
