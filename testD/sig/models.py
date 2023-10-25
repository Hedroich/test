from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    date_publishing = models.DateField(auto_now_add=True)


class Task  (models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=256)
    priority = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
