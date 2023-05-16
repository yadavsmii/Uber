from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import *
from users.serializers import *
class GetStudentsView(APIView):
    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance = Students.objects.filter(first_name=name)
        else:
            instance = Students.objects.all()    
        Serializer = StudentsSerializers(instance,many=True)
        return Response(Serializer.data)
    def post(self,request):
        params = request.data
        print("params",params)
        serializers = StudentsSerializers(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message","Done"})
class GetOrdersView(APIView):
    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance = Orders.objects.filter(order_name=name)
        else:
            instance = Orders.objects.all()    
        Serializer = OrdersSerializers(instance,many=True)
        return Response(Serializer.data)
    def post(self,request):
        params = request.data
        print("params",params)
        serializers = OrdersSerializers(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message","Done"})    