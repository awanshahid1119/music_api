# users/urls.py

from django.urls import path
from .views import UserListView, UserProfileDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='user-detail'),
]
