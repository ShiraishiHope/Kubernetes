from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('1', 'Élevée'),
        ('2', 'Moyenne'),
        ('3', 'Faible'),
    ]

    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='2', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title