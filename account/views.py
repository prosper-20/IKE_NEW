from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from .serializers import UserRegistrationSerialier
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerialier
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = UserRegistrationSerialier(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Message": "Account creation successful",
                         "username": user.username,
                         "email": user.email,
                         "token": token.key})
