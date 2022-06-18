from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET', 'PUT'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
