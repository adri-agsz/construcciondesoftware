from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

# Create your views here.
def index(request):
    #return HttpResponse('<h1> Bienvenidos a la sesión de hoy! </h1>')
    return render(request, 'index.html')

def adrian(request):
    return HttpResponse('<h1> Hola Adrián! </h1>')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola ' + nombre)

def bienvenida(request):
    letrero = "Bienvenida"
    return HttpResponse(letrero)

def multiplicacion(request):
    p =int(request.GET['p'])
    q = int(request.GET['q'])

    return HttpResponse(f"la multiplicacion de {p} y {q} es {p*q}")
    

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    p = body['p']
    q = body['q']
    resultado = Fraccion(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, content_type = "text/json-comment-filtered")