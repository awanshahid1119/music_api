# users/views.py

from rest_framework import generics, permissions 
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import IsOwnerOrReadOnly

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
