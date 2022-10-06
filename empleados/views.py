from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index_empleados(request):
    return render(request, 'empleados/index_empleados.html')


