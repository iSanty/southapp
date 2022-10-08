from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index_new.html')


@login_required
def error(request):
    return render(request, '404.html')