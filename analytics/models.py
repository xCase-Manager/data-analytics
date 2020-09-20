import datetime

from django.db import models
from django.utils import timezone

class Job(models.Model):
    name = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name + " : " + self.tags

    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

class Execution(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    execution_tags = models.CharField(max_length=200)
    execution_status = models.CharField(max_length=50, default = "NOT RUN")
    start_date = models.DateTimeField('date started', default=timezone.now())
    finish_date = models.DateTimeField('date finished')

    def __str__(self):
        return self.tags + " : " + self.status