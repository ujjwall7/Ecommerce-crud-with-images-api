from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ecommerce
from .serializer import EcommerceSerializer

#hariom

class EcommerceAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            stu=Ecommerce.objects.get(id=id)
            serializer=EcommerceSerializer(stu)
            return Response(serializer.data)

        stu = Ecommerce.objects.all() 
        serializer = EcommerceSerializer(stu, many=True) 
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=EcommerceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

    def put(self,request,pk,format=None):
        id = pk 
        stu = Ecommerce.objects.get(id=id) 
        serializer = EcommerceSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({ 'msg' : 'Complete Data Updated'}) 
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,format= None):
        id = pk 
        stu = Ecommerce.objects.get(id=id)
        serializer = EcommerceSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({ 'msg' : 'Partial Data Updated'}) 
        return Response (serializer.errors)


    def delete(self, request, pk, format=None):
        id = pk 
        stu = Ecommerce.objects.get(pk=id) 
        stu.delete() 
        return Response({'msg' : 'Data Deleted' })


    