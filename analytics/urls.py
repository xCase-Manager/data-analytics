from rest_framework import routers
from analytics.views import (
    executions, jobs, users)


router = routers.DefaultRouter()
router.register(r'jobs', jobs.JobViewSet)
router.register(r'executions', executions.ExecutionViewSet)
router.register(r'users', users.UserViewSet)
router.register(r'groups', users.GroupViewSet)

urlpatterns = router.urls