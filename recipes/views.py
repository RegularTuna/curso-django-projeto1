from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Tiago Fortuna'
    })

def contacto(request):
    return render(request, 'temp/temp.html')

def sobre(request):
    return HttpResponse("sobre")