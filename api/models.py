from django.db import models

class Task(models.Model):
    tittleTask=models.CharField (max_length=50)
    descriptionTask=models.CharField (max_length=200)
    priorityTask=models.PositiveBigIntegerField()