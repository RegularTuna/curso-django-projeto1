from django.contrib import admin
from django.urls import path
from recipes.views  import home, contacto, sobre




urlpatterns = [
    path('admin/', admin.site.urls),   
    path('',home), #Home
    path('sobre/',sobre), #Sobre
    path('contacto/',contacto) #contacto
]
