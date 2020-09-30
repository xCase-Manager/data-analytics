from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import json
from analytics.serializers import (JobSerializer, ExecutionSerializer, 
    UserSerializer, GroupSerializer) 
from .models import Job, Execution
import pandas as pd


def dashboard(request):
    """
    Dashboard jobs list
    """
    jobs_orm = Job.objects.values()
    jobs_pandas = pd.DataFrame(jobs_orm)
    return JsonResponse(json.loads(jobs_pandas.to_json()), 
        safe=False)

def executions(request):
    """
    Execution analytics
    """
    return _jsonResponse(_getExecutionsList()
        .set_index(["tags", "status"])
        .count(level="status")
        .to_json())

def _getExecutionsList():
    """
    get executions list
    """
    executions_orm = Execution.objects.values()
    return pd.DataFrame(executions_orm)

def _jsonResponse(payload):
    """
    response formatter
    """
    return JsonResponse(
        json.loads(payload), 
        safe=False)

def executions(request):
    """
    Execution analytics
    """
    return JsonResponse(
        json.loads(_getExecutionsList()
        .set_index(["tags", "status"])
        .count(level="status")
        .to_json()), 
        safe=False)

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