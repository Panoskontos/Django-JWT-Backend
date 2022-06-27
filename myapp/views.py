from urllib import response
from django.shortcuts import render
from matplotlib.pyplot import cla
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
# JWT
import jwt,datetime

# Register
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Login and create cookies
class LoginView(APIView):
    def post(self, request):
        name = request.data['name']
        password = request.data['password']

        user = User.objects.filter(name=name,password=password).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        payload = {
            'id': user.id,
            # when it expires
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            # when it was created
            'iat': datetime.datetime.now(),
        }

        token = jwt.encode( payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt',value=token, httponly=True)
        response.data =  {
            'message':'success', 
            'jwt':token
            }
        return response


# Get User
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated, You have to login again")

        print(payload['id'])
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


# Logout
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'You have logged out'
        }
        return response