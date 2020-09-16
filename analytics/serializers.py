from django.contrib.auth.models import User, Group
from .models import Execution
from rest_framework import serializers


class ExecutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Execution
        fields = ['execution_tag', 'creation_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']