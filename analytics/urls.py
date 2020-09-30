from django.urls import include, path, re_path
from django.conf.urls import url 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'executions', views.ExecutionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls