from django.shortcuts import render
from .models import Treasure, Profile
from .serializers import TreasureSerializer, ProfileSerializer
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class TreasureViewSets(viewsets.ModelViewSet):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
            
    
class ProfileViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
