from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

account_sid = 'ACfaa88aace5e1a8c3d3ca209c27fb669a'
auth_token = 'f016c9b285c959eddc1681c18edf9175'
client = Client(account_sid, auth_token)




@csrf_exempt
def bot(request):
    
    
    print(request.POST)
   
                        
    
    return HttpResponse("Hola, como estas?")