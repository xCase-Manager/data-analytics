from django.db import models


class Execution(models.Model):
    Execution_tag = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Result(models.Model):
    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    result_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')