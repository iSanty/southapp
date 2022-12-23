from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from api.api import solicitud_oca

account_sid = 'ACa59cfbea3b70499efe3235beb84ecc01'
auth_token = '242de0cee777d5fa0b9c66781e67b63f'
client = Client(account_sid, auth_token)


def bot(request):
    
    if request.method =="POST":
        mensaje = request.POST["Body"]
        numero = request.POST["From"]
        
        
        
        print(mensaje)
        print(numero)
        if mensaje =="Join walk-careful":
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="""Hola, bienvenido al bot de Southpost, responda con el numero de opcion deseada:
1: Consulta pedido OCA
2: Cancelar envio
3: Comunicarme con un representante de atencion al cliente"""
                
                ,
                to=numero
            )
            
        elif mensaje == '1':
            accion = 'buscar'
            client.messages.create(
                from_='whatsapp:+14155238886',
                body='Por favor indique su numero de OCA',
                
                to=numero                
            
            
            )
        elif mensaje == '2':
            accion = 'cancelar'
            client.messages.create(
                from_='whatsapp:+14155238886',
                body='Por favor indique su numero de ID o GUIA',
                
                to=numero                
            
            
            )
            
        elif mensaje == '3':
            accion = 'llamar'
            client.messages.create(
                from_='whatsapp:+14155238886',
                body='Para comunicarse con un representante de atencion al cliente por favor comuniquese al número 08103457678 opcion 2, de 09 a 17hs',
                
                to=numero                
            
            
            )
        elif mensaje:
            accion = 'Consulta OCA'
            
            consulta = solicitud_oca(mensaje)
            
            if consulta != 'Error':
                nro_guia = consulta[1]
                estado_pieza = consulta[0]
                
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='Su numero de guia SP es '+ nro_guia+ ' y su pedido se encuentra '+ estado_pieza,
                    
                    to=numero                
                
                
                )
            else:
                
                client.messages.create(
                from_='whatsapp:+14155238886',
                body="""Hola, bienvenido al bot de Southpost, responda con el numero de opcion deseada:
1: Consulta pedido OCA
2: Cancelar envio
3: Comunicarme con un representante de atencion al cliente"""
                
                ,
                to=numero
            )
            
            
            
            
        else:
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="""Hola, bienvenido al bot de Southpost, responda con el numero de opcion deseada:
1: Donde esta mi paquete 
2: Cancelar envio
3: Comunicarme con un representante de atencion al cliente""",
                
                to=numero                
            
            
            )
                
    return HttpResponse('Sistema de comunicacion por Whatsapp con clientes finales.')
    
    
    
    