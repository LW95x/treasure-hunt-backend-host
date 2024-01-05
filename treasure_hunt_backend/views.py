from django.shortcuts import render
from .models import Treasure, Profile
from django.contrib.auth.models import User
from .serializers import TreasureSerializer, ProfileSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False}, status=401)

# from .. import schema
# from django.http import HttpResponse


# def read_file(schema):
#     with open(schema, 'r') as file:
#         return file.read()

# def file_view(req):
#     yaml_file = read_file(schema)
#     return HttpResponse(yaml_file, content_type='text/plain')



class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TreasureViewSets(viewsets.ModelViewSet):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer