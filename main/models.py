from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=15)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    users = models.ManyToManyField(User, related_name="projects")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="projects_created")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.project_name
