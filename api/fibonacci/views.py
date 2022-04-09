from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.fibonacci.serializers import FibonacciSerializer


class FibonacciValue(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = FibonacciSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(dict(success=False, errors=[serializer.errors]), status=status.HTTP_400_BAD_REQUEST)
