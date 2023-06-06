from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from tierra.models import usuario, rol
from .serializer import usuarioserializer, rolserializer
@csrf_exempt
@api_view(['GET','POST'])
def lista_usuario(request):

    if request.method == 'GET':
        usuario = usuario.objects.all()
        serializer = usuarioserializer(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().perse(request)
        serializer = usuarioserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def lista_rol(request):

    if request.method == 'GET':
        rol = rol.objects.all()
        serializer = rolserializer(rol, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().perse(request)
        serializer = rolserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Create your views here.
