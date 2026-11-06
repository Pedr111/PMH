from django.shortcuts import render


def inicio(request):
    return render(request, 'Martinez/Inicio.html')
