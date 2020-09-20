from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from analytics.serializers import JobSerializer, ExecutionSerializer, UserSerializer, GroupSerializer 
from .models import Job, Execution


def index(request):
    latest_execution_list = Execution.objects.order_by('creation_date')[:5]
    output = ', '.join([execution.execution_tag for execution in latest_execution_list])
    return HttpResponse(output)


class JobViewSet(viewsets.ModelViewSet):
    """
    Jobs list
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExecutionViewSet(viewsets.ModelViewSet):
    """
    Executions list
    """
    queryset = Execution.objects.all()
    serializer_class = ExecutionSerializer
    permission_classes = [permissions.IsAuthenticated]

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