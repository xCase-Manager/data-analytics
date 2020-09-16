import datetime

from django.db import models
from django.utils import timezone


class Execution(models.Model):
    execution_tag = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.execution_tag

    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

class Result(models.Model):
    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    result_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')

    def __str__(self):
        return self.result_text