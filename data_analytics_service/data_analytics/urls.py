from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('data_analytics/', include('data_analytics.urls')),
    path('admin/', admin.site.urls),
]