from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'priority', 'created_at', 'completed_at')
    list_filter = ('is_completed', 'priority')
    search_fields = ('title',)