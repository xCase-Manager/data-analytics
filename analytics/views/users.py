from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from analytics.serializers import (
    UserSerializer, GroupSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    Users list
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    Groupds list
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]