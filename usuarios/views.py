from django.shortcuts import render
from usuarios.models import Usuarios
# Create your views here.


def userlist(request):

    usr_list= Usuarios.objects.all()

    context= {"users":usr_list}

    return render(request, "usuarios.html", context)



