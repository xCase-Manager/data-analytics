from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'executions', views.ExecutionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('executions', views.executions, name='executions'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]