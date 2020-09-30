from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
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

@api_view(['GET'])
def executions(request):
    """
    Execution analytics
    """
    if request.method == 'GET':
        return _jsonResponse(_getExecutionsList()
            .set_index(["tags", "status"])
            .count(level="status")
            .to_json())

def executionsFinish(request):
    """
    Execution analytics
    """
    return _jsonResponse(_getExecutionsList()
        .set_index(["tags", "finish_date"])
        .count(level="finish_date")
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

    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_executions = Execution.objects.all().order_by('start_date')
        serializer = ExecutionSerializer(recent_executions, 
            context={'request': request},
            many=True)
        return Response(serializer.data)


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