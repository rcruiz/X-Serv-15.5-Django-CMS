from django.shortcuts import render
from django.http import HttpResponse
from models import Pages


def mostrar_id(request, page_id):
    try:
        contenido = Pages.objects.get(id=int(page_id))
        return HttpResponse(contenido.name + ' -> ' + contenido.page)
    except Pages.DoesNotExist:
        return HttpResponse('Pagina no encontrada')


def mostrar_name(request, recurso):
    try:
        contenido = Pages.objects.get(name=recurso)
        return HttpResponse(contenido.page)
    except Pages.DoesNotExist:
        return HttpResponse('Pagina no encontrada')
