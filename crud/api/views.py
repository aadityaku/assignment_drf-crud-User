from django.shortcuts import render

# Create your views here.
from .models import Todo
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

#for new User create 
class Register(APIView):

    def post(self,request):
        serializer=RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TodoView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
       
        if id != None: #single task retrive
            todo=Todo.objects.get(pk=id)
            serializer=TodoSerializer(todo,many=False)
            return Response(serializer.data)

        task=Todo.objects.all() #all task retrive
        serializer=TodoSerializer(task,many=True)
        return Response(serializer.data)
    
    #New task create
    def post(self,request):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #task is update
    def put(self,request,id):
        task=Todo.objects.get(pk=id)
        serializer=TodoSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    #task is deleted
    def delete(self,request,id):
        task=Todo.objects.get(pk=id)
        task.delete()
        return Response("Task deleted successfully")

  
    

