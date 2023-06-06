from django.urls import path
from .views import lista_usuario

urlpatterns =[
    path('lista_usuarios',lista_usuario, name="lista_usuario"),
]


