from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
import json, pandas as pd
from analytics.serializers import JobSerializer 
from analytics.models import Job


class JobViewSet(viewsets.ModelViewSet):
    """
    Jobs view
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        filtered by date
        """
        recent_jobs = Job.objects.all().order_by('creation_date')
        serializer = JobSerializer(recent_jobs, 
            context={'request': request},
            many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def tags(self, request):
        """
        filtered by tags
        """
        return self._jsonResponse(self._getList()
            .set_index(["name", "tags"])
            .count(level="tags")
            .to_json())

    def _getList(self):
        """
        get executions list
        """
        executions_orm = Job.objects.values()
        return pd.DataFrame(executions_orm)
    
    def _jsonResponse(self, payload):
        """
        response formatter
        """
        return JsonResponse(
            json.loads(payload), 
            safe=False)