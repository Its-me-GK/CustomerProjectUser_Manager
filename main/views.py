from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Client, Project
import json

@csrf_exempt
def clients_list(request):
    if request.method == "GET":
        clients = Client.objects.all().values("id", "client_name","client_phone","client_email", "created_by","created_at", "updated_at")
        return JsonResponse(list(clients), safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        client = Client.objects.create(
            client_name=data["client_name"],
            client_phone=data["client_phone"],
            client_email=data["client_email"],
            created_by=request.user if request.user.is_authenticated else None
        )
        return JsonResponse({
            "id": client.id,
            "client_name": client.client_name,
            "client_phone": client.client_phone,
            "client_email": client.client_email,
            "created_at": client.created_at,
            "created_by": client.created_by.username if client.created_by else None
        })


@csrf_exempt
def client_detail(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return JsonResponse({"error": "Client not found"}, status=404)

    if request.method == "GET":
        projects = []
        for project in client.projects.all():
            projects.append({
                "id": project.id,
                "name": project.project_name,
                "users": list(project.users.values("id", "username"))
            })
            
        return JsonResponse({
            "id": client.id,
            "client_name": client.client_name,
            "client_email": client.client_email,
            "client_phone": client.client_phone,
            "projects": projects,
            "created_at": client.created_at,
            "created_by": client.created_by.username if client.created_by else None,
            "updated_at": client.updated_at,
        })

    elif request.method == "PUT" or request.method == "PATCH":
        data = json.loads(request.body)
        client.client_name = data.get("client_name", client.client_name)
        client.client_phone = data.get("client_phone", client.client_phone) 
        client.client_email = data.get("client_email", client.client_email)
        client.save()
        return JsonResponse({
            "id": client.id,
            "client_name": client.client_name,
            "client_email": client.client_email,
            "client_phone": client.client_phone,
            "created_at": client.created_at,
            "created_by": client.created_by.username if client.created_by else None,
            "updated_at": client.updated_at,
        })

    elif request.method == "DELETE":
        client.delete()
        return JsonResponse({}, status=204)

@csrf_exempt
def create_project(request, client_id):
    if request.method == "POST":
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return JsonResponse({"error": "Client not found"}, status=404)

        data = json.loads(request.body)
        project = Project.objects.create(
            project_name=data["project_name"],
            project_description=data["project_description"],
            client=client,
            created_by=request.user if request.user.is_authenticated else None
        )
        project.users.set(User.objects.filter(id__in=[u["id"] for u in data["users"]]))
        return JsonResponse({
            "id": project.id,
            "project_name": project.project_name,
            "client": client.client_name,
            "users": list(project.users.values("id", "username")),
            "created_at": project.created_at,
            "created_by": project.created_by.username if project.created_by else None,
        })


def my_projects(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    projects = request.user.projects.all().values("id", "project_name","project_description", "created_at")
    return JsonResponse(list(projects), safe=False)
