from django.contrib import admin
from .models import Project, Task

# Register your models here.
@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date_publishing")


@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "priority")