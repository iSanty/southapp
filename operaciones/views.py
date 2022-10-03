from django.shortcuts import render

# Create your views here.

def index_productos(request):
    return render(request, 'operaciones/operaciones.html')