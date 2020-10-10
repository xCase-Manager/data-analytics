from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from analytics.serializers import ExecutionSerializer
from analytics.models import Job, Execution
from .view import View
  
class ExecutionViewSet(View):
    """
    Executions list
    """
    queryset = Execution.objects.all()
    serializer_class = ExecutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        ordered by date 
        """
        recent_executions = Execution.objects \
            .all().order_by('start_date')
        serializer = ExecutionSerializer(recent_executions, 
            context={'request': request},
            many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def finished(self, request):
        """
        filtered by finish date
        """
        return self._filter(Execution.objects.values(), 
            "tags", "finish_date")

    @action(detail=False, methods=['get'])
    def status(self, request):
        """
        filtered by status
        """
        return self._filter(Execution.objects.values(),
            "tags", "status")