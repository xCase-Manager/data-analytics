import datetime

from django.db import models
from django.utils import timezone

class Job(models.Model):
    name = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    creation_date = models.DateTimeField('created date', default=None, blank=True, null=True)
    update_date = models.DateTimeField('updated date', default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

class Execution(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default = "NOT RUN")
    start_date = models.DateTimeField('date started', default=None, blank=True, null=True)
    finish_date = models.DateTimeField('date finished', default=None, blank=True, null=True)