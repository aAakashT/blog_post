from django.shortcuts import render
from rest_framework import authentication, permissions 
from rest_framework.permissions import IsAuthenticated, AllowAny  
from rest_framework.authentication import TokenAuthentication 
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Formality(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, id):
        token = request.token
        return Response({"hello": f"{token}"})
    