from django.shortcuts import render


def index(request):
    return render(request, 'index_new.html')



def error(request):
    return render(request, '404.html')