# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenue sur ma To-Do List </h1><p>Ceci est une page d'exemple.</p>")
