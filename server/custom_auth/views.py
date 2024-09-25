from urllib.request import Request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, StaticHTMLRenderer


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def login(request):
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)