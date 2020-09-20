from django.contrib.auth.models import User, Group
from .models import Job, Execution
from rest_framework import serializers


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'tags', 'creation_date']


class ExecutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Execution
        fields = ['id', 'job_id', 'tags', 'status', 'start_date', 'status']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']