from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from api.api import solicitud_oca, solicitud_presis
from .models import Accion, MensajePorEstado
from .forms import frmMensajePorEstado

account_sid = 'ACa59cfbea3b70499efe3235beb84ecc01'
auth_token = '242de0cee777d5fa0b9c66781e67b63f'
client = Client(account_sid, auth_token)


def bot(request):
    
    
    if request.method =="POST":
        mensaje = request.POST["Body"]
        numero = request.POST["From"]
        
        accion = Accion.objects.filter(numero=numero)
        
        if accion:
            accion = Accion.objects.get(numero=numero)
        else:
            nuevo = Accion(
                    numero = numero,
                    accion = 'inicio'
                )
            nuevo.save()
    
    
        if mensaje == 'Hola' or mensaje == 'HOla' or mensaje == 'hola':
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="""Hola, bienvenido al bot de Southpost, responda con el numero de opcion deseada:
1: Consulta estado e-presis
2: Consultar por nro pedido OCA
""",
                to=numero
            )
            accion = Accion.objects.filter(numero=numero)
            if accion:
                accion = Accion.objects.get(numero=numero)
                accion.accion = 'inicio'
                accion.save()
            else:
                nuevo = Accion(
                    numero = numero,
                    accion = 'inicio'
                )
                nuevo.save()
            
            
        elif mensaje == '1' and accion.accion == 'inicio':
            accion = Accion.objects.get(numero=numero)
            accion.accion = 'epresis'
            accion.save()
            
            client.messages.create(
                from_='whatsapp:+14155238886',
                body='Por favor indique el numero de guia. "EJ: 2611423"',
                
                to=numero                
            )
            print(accion.accion)
        elif mensaje == '2' and accion.accion == 'inicio':
            
            accion = Accion.objects.get(numero=numero)
            accion.accion = 'oca'
            accion.save()
            
            client.messages.create(
                from_='whatsapp:+14155238886',
                body='Por favor indique el numero de envio de oca. EJ: "2433486"',
                
                to=numero                
            )
            
            
        elif mensaje != '1' or mensaje != '2' or mensaje != '3':
            
            accion = Accion.objects.filter(numero=numero)
            print(accion)
            if accion:
                accion = Accion.objects.get(numero=numero)
            
            
            
                if accion.accion == 'epresis':
                    consulta = solicitud_presis(mensaje)
                
                    if consulta:
                        estado = consulta['estado']
                        fecha = consulta['fecha']
                        # fecha_pactada = consulta['fecha_pactada']
                        
                        mensajes = MensajePorEstado.objects.filter(estado=estado)
                        
                        if mensajes:
                            respuesta = MensajePorEstado.objects.get(estado=estado)
                            
                            if respuesta.estado == 'PENDIENTE DE STOCK':
                                client.messages.create(
                                    from_='whatsapp:+14155238886',
                                    body=f'{respuesta.mensaje} Estado: {respuesta.estado}',
                                    
                                    to=numero                
                                    
                                    
                                    )
                                accion.accion = 'inicio'
                                accion.save()
                            elif respuesta.estado == 'ARMADO':
                                client.messages.create(
                                    from_='whatsapp:+14155238886',
                                    body=f'{respuesta.mensaje} Estado: {respuesta.estado}',
                                    
                                    to=numero                
                                    
                                    
                                    )
                                accion.accion = 'inicio'
                                accion.save()
                                
                            elif respuesta.estado == 'PROGRAMACION':
                                client.messages.create(
                                    from_='whatsapp:+14155238886',
                                    body=f'{respuesta.mensaje} Estado: {respuesta.estado}',
                                    
                                    to=numero                
                                    
                                    
                                    )
                                accion.accion = 'inicio'
                                accion.save()
                                
                            elif respuesta.estado == '1° Visina no responde.':
                                client.messages.create(
                                    from_='whatsapp:+14155238886',
                                    body=f'{respuesta.mensaje} Estado: {respuesta.estado}',
                                    
                                    to=numero                
                                    
                                    
                                    )
                                accion.accion = 'inicio'
                                accion.save()
                            else:
                        
                                client.messages.create(
                                    from_='whatsapp:+14155238886',
                                    body=f'Su pedido se encuentra en estado {estado} desde la fecha {fecha}.',
                                    
                                    to=numero                
                                    
                                    
                                    )
                            accion.accion = 'inicio'
                            accion.save()
                            
                        
                        else:
                            client.messages.create(
                                from_='whatsapp:+14155238886',
                                body=f'Su pedido se encuentra en estado {estado} desde la fecha {fecha}.',
                                
                                to=numero                
                                
                                
                                )
                            accion.accion = 'inicio'
                            accion.save()
                    else:
                        client.messages.create(
                        from_='whatsapp:+14155238886',
                        body="""Si estas ingresando tu numero de seguimiento, antes tenes que responder la opcion deseada:
1: Consulta estado e-presis
2: Consultar por nro pedido OCA
""",
to=numero)
                        accion = Accion.objects.filter(numero=numero)
                        if accion:
                            accion = Accion.objects.get(numero=numero)
                            accion.accion = 'inicio'
                            accion.save()
                        else:
                            nuevo = Accion(
                                numero = numero,
                                accion = 'inicio'
                            )
                            nuevo.save()
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
                elif accion.accion == 'oca':
                    consulta = solicitud_oca(mensaje)
                    
                    
                    nro_guia = consulta[1]
                    estado_pieza = consulta[0]
                    
                    client.messages.create(
                        from_='whatsapp:+14155238886',
                        body='Su numero de guia SP es '+ nro_guia + ' y su pedido se encuentra '+ estado_pieza,
                        
                        to=numero                
                        
                        
                        )
                    accion.accion = 'inicio'
                    accion.save()
                    
                else:
                    client.messages.create(
                        from_='whatsapp:+14155238886',
                        body="""Si estas ingresando tu numero de seguimiento, antes tenes que responder la opcion deseada:
1: Consulta estado e-presis
2: Consultar por nro pedido OCA
""",
to=numero)
                    accion = Accion.objects.filter(numero=numero)
                    if accion:
                        accion = Accion.objects.get(numero=numero)
                        accion.accion = 'inicio'
                        accion.save()
                    else:
                        nuevo = Accion(
                            numero = numero,
                            accion = 'inicio'
                        )
                        nuevo.save()
            
            
        else:
            
            client.messages.create(
            from_='whatsapp:+14155238886',
            body="""Si estas ingresando tu numero de seguimiento, antes tenes que responder la opcion deseada:
1: Consulta estado e-presis
2: Consultar por nro pedido OCA
""",
            to=numero
        )
            accion = Accion.objects.filter(numero=numero)
            if accion:
                accion = Accion.objects.get(numero=numero)
                accion.accion = 'inicio'
                accion.save()
            else:
                nuevo = Accion(
                    numero = numero,
                    accion = 'inicio'
                )
                nuevo.save()
            
    
    
    print(accion)
    return HttpResponse(accion)
    
    
    
    
    
def crear_mensaje_por_estado(request):
    
    
    form = frmMensajePorEstado()
    
    if request.method == 'POST':
        form = frmMensajePorEstado(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            en_base = MensajePorEstado.objects.filter(estado=data['estado'])
            if en_base:
                mensaje = MensajePorEstado.objects.get(estado=data['estado'])
                mensaje.estado = data['estado']
                mensaje.mensaje = data['mensaje']
                mensaje.save()
                msj = 'Mensaje por editado correctamente'
                return render(request, 'bot/parametros.html', {'form':form, 'msj':msj})
                
            else:
                mensaje = MensajePorEstado(
                    estado = data['estado'],
                    mensaje = data['mensaje']
                )
                mensaje.save()
                msj = 'Mensaje por estado creado correctamente'
                return render(request, 'bot/parametros.html', {'form':form, 'msj':msj})
            
    else:
        
        return render(request, 'bot/parametros.html', {'form':form})
            
    
    return render(request, 'bot/parametros.html', {'form':form})

