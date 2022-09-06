from django.shortcuts import render

# Create your views here.


def index_transportes(request):
    return render(request, 'index.html')