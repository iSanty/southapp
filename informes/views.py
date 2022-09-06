from django.shortcuts import render


def index_informes(request):
    return render(request, 'index.html')