from .models import Treasure, Profile
from django.contrib.auth.models import User
from .serializers import TreasureSerializer, ProfileSerializer, UserSerializer, LoginSerializer
from rest_framework import viewsets, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                return Response({'success': True}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # def create(self, request, *args, **kwargs):
    #     return Response({"detail": "Creating new profiles isn't allowed, create a user instead."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Deleting existing profiles isn't allowed, delete the user instead."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class TreasureViewSets(viewsets.ModelViewSet):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer

    def update(self, request, *args, **kwargs):
        treasure = self.get_object()
        if 'increment_collected_by' in request.data:
            treasure.collected_by += 1
            treasure.save()

        return super().update(request, *args, **kwargs)