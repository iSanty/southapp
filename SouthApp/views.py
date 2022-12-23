from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
from django.http.response import HttpResponse



account_sid = 'AC0e085fdb45b6508a50de706b8257a337'
auth_token = '005fb71cb00230e2e3b696db06dfc94b'
client = Client(account_sid, auth_token)





def index(request):
    
    
    
    return render(request, 'index.html')


@login_required
def error(request):
    return render(request, '404.html')