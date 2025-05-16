from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def is_due_soon(self):
        if self.due_date:
            now = timezone.now()
            return (self.due_date - now).days <= 2 and self.status != 'completed'
        return False
    
    def is_overdue(self):
        if self.due_date:
            return self.due_date < timezone.now() and self.status != 'completed'
        return False