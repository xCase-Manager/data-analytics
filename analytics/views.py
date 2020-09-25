from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from analytics.serializers import JobSerializer, ExecutionSerializer, UserSerializer, GroupSerializer 
from .models import Job, Execution
import pandas as pd


def dashboard(request):
    """
    Dashboard jobs list
    """
    jobs_orm = Job.objects.values()
    jobs_pandas = pd.DataFrame(jobs_orm)
    return JsonResponse(jobs_pandas.to_json(), safe=False)

def executions(request):
    """
    Execution analytics
    """
    executions_orm = Execution.objects.values()
    executions_pandas = pd.DataFrame(executions_orm)
    return JsonResponse(executions_pandas.set_index(["tags", "status"])
        .count(level="status")
        .to_json(), safe=False)

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