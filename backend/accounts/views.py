from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegisterSerializer


@api_view(['POST'])
def register(request):

    serializer = RegisterSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response({
            'message':
            'Registration Successful'
        })

    return Response(serializer.errors)


@api_view(['POST'])
def login(request):

    username = request.data.get(
        'username'
    )

    password = request.data.get(
        'password'
    )

    user = authenticate(
        username=username,
        password=password
    )

    if user:

        return Response({

            'message':
            'Login Successful',

            'username':
            user.username
        })

    return Response({

        'error':
        'Invalid Credentials'
    })