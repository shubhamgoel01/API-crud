from django.shortcuts import render
import requests
from django.http import HttpResponse, response
from django.shortcuts import get_list_or_404      
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Add_category, Add_subcategory, Add_icard
from .serializers import Add_categorySerializer, Add_subcategorySerializer, Add_icardSerializer



class Icard(APIView):   
    def get(self, request , pk=None): 
        if pk is not None:
            id = pk
            cat = Add_category.objects.get(id = id)
            serializer = Add_categorySerializer(cat)
        else:
            category = Add_category.objects.all()   
            serializer = Add_categorySerializer(category, many=True) 
        return Response(serializer.data)       
 
    
    def post(self,request):
        serializer = Add_categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self ,request , pk ):
        id = pk
        cat = Add_category.objects.get(id = id)
        cat.delete()
        return Response({'reply':'data is deleted'})
        

    def put(self ,request , pk = None , format = None):    
        id = pk    
        cat= Add_category.objects.get(id = id)
        serializer = Add_categorySerializer(cat , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'reply':"data is updated"})
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

    


  























