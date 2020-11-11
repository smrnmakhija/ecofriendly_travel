from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Trip
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.exceptions import APIException
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer


# Create your views here.

class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecofriendly/project_index.html'

    def get(self, request):
        """
        List all skus
        """
        users = User.objects.all()
        return Response({
            'users': users
            })
