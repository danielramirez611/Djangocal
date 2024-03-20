from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Realiza tus operaciones aqui..")

def suma (request, num1,num2):
    calculo=int(num1) + int(num2)
    resultado =f"La suma de {num1}+ {num2} es {calculo}"
    return HttpResponse(resultado)

def resta (request, num1,num2):
    calculo=int(num1) - int(num2)
    resultado =f"La resta de {num1}- {num2} es {calculo}"
    return HttpResponse(resultado)


def multiplicacion (request, num1,num2):
    calculo=int(num1) * int(num2)
    resultado =f"La multiplicaci+ón de {num1}* {num2} es {calculo}"
    return HttpResponse(resultado)