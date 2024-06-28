from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.core import serializers
from django.http import HttpResponse

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited
    """

    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated
    
    def create(self, request):
        # Use request.data instead of request.POST to get the data
        task_title = request.data.get('title')
        task_description = request.data.get('description')
        task_user = request.user
        
        # Create the Todo instance
        todo = Todo.objects.create(title=task_title, description=task_description, user=task_user)
        
        # Serialize the created Todo instance
        serialized_obj = serializers.serialize('json', [todo, ])
        
        # Return the serialized object as JSON response
        return HttpResponse(serialized_obj, content_type='application/json')