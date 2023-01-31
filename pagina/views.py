from django.shortcuts import render

# Create your views here.



def index_pagina(request):
    
    return render(request, 'pagina/index_pagina.html')
