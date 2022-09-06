from django.shortcuts import render

# Create your views here.
def index_accounts(request):
    return render(request, 'index.html')