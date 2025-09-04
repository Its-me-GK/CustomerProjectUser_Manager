from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.clients_list, name="clients_list"),
    path("clients/<int:client_id>/", views.client_detail, name="client_detail"),
    path("clients/<int:client_id>/projects/", views.create_project, name="create_project"),
    path("projects/", views.my_projects, name="my_projects"),
]
