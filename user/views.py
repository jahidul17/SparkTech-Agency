from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .import serializers
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth.tokens import default_token_generator

def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }


class RegisterAdminApiView(APIView):
    serializer_class=serializers.RegisterAdminSerializers
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            tokens=get_tokens_for_user(user)
            
            return Response({
                "User Name":user.username,
                "First Name":user.first_name,
                "Last Name":user.last_name,
                "Email":user.email,
                "tokens":tokens,
            },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)


class RegisterUserApiView(APIView):
    serializer_class=serializers.RegisterUserSerializers
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            tokens=get_tokens_for_user(user)
            
            return Response({
                "User Name":user.username,
                "First Name":user.first_name,
                "Last Name":user.last_name,
                "Email":user.email,
                "tokens":tokens,
            },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)





class LoginApiView(APIView):    
    
    def post (self,request):
        serializer=serializers.UserLoginSerializers(data=self.request.data)
        
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            
            user=authenticate(username=username,password=password)
            
            if user is not None:
                tokens=get_tokens_for_user(user)
                return Response({
                    # "user":serializers.UserLoginSerializers(user).data,
                    "User Name":user.username,
                    "First Name":user.first_name,
                    "Email":user.email,
                    "tokens":tokens,
                },status=status.HTTP_200_OK)
            else:
                return Response({'error':"Invalid Credential"})
        return Response(serializer.errors)
                



class LogOutApiview(APIView):
    def post(self,request):
        try:
            refresh_token=request.data.get('refresh')
            if not refresh_token:
                return Response({'error':"No refresh token provided"},status=status.HTTP_400_BAD_REQUEST)
            token=RefreshToken(str(refresh_token))
            token.blacklist()
            return Response({"message":"Successfully logged out!"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":"Invalid token"},status=status.HTTP_400_BAD_REQUEST)
        

class TokenRefreshApiView(APIView):
    def post(self,request):
        try:
            refresh_token=request.data.get('refresh')
            token=RefreshToken(refresh_token)
            new_access_token=str(token.access_token)
            return Response({"access":new_access_token},status=status.HTTP_200_OK)  
        except Exception as e:
            return Response({"error":"An unexpected error occurred"},status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  

  
            