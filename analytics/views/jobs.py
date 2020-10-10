from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from analytics.serializers import JobSerializer 
from analytics.models import Job
from .view import View


class JobViewSet(View):
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
        recent_jobs = Job.objects \
            .all().order_by('creation_date')
        serializer = JobSerializer(recent_jobs, 
            context={'request': request},
            many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def tags(self, request):
        """
        filtered by tags
        """
        return self._filter(Job.objects.values(), 
            "name", "tags")