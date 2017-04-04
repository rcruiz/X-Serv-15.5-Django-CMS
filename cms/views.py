from django.shortcuts import render
from django.http import HttpResponse
from .models import Page


def mostrar_id(request, page_id):
    try:
        contenido = Page.objects.get(id=int(page_id))
        return HttpResponse(contenido.name + ' : ' + contenido.page)
    except Page.DoesNotExist:
        return HttpResponse('Pagina no encontrada')


def mostrar_name(request, recurso):
    try:
        contenido = Page.objects.get(name=recurso)
        return HttpResponse(contenido.page)
    except Page.DoesNotExist:
        return HttpResponse('Nombre de la página no almacenado')
