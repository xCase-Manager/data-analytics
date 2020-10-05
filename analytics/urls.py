from rest_framework import routers
from analytics.views import (
    views, executions, jobs)


router = routers.DefaultRouter()
router.register(r'jobs', jobs.JobViewSet)
router.register(r'executions', executions.ExecutionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls