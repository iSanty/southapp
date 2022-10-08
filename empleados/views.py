from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index_meli(request):
    return render(request, 'empleados/index_meli.html')


def linkeo(request):
    return render(request, 'index_new.html')


