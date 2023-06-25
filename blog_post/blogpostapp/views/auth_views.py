# from rest_framework import 
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView

class ApiLogin(APIView):
    def post(self, request):
        data = request.data
        authenticated = authenticate(data)
        if authenticated:
            try:
                login(email=request.email, password=request.password)
            except Exception:
                return Response({'error': 'wrong credentials'})    