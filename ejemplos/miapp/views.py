from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    respu= "<ul>"
    respu= respu + "<li>elemento 1</li>"
    respu= respu + "<li>elemento 2</li>"
    respu= respu +"</ul>"
    return HttpResponse(respu)

def nuevococinero(request):
    return HttpResponse("<p color=>Esto es para el nuevo cocinero</p>")

def consultarpedido(request):
    return HttpResponse("Este es el pedido")
def primero(request):
    return HttpResponse("<h1>Primer ejemplo</h1><p></p><center><h2>Hola</h2>")
def segundo(request):
    return HttpResponse("<H1>Segundo ejemplo</h1><p></p><center><h2>Mundo</h2>")   
def tercero(request):
    return HttpResponse("<H1>Tercer ejemplo</h1><p></p><center><h2>Soy</h2>") 
