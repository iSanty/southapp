from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index_informes(request):
    return render(request, 'index_new.html')