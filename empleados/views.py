from django.shortcuts import render

# Create your views here.
def index_empleados(request):
    return render(request, 'index.html')