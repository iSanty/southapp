from django.http import HttpResponse
from django.views.decorators.http import require_POST
# Create your views here.
from datetime import datetime, date, timedelta


from informes.models import GlobalPK


@require_POST
def nuevo_global(request, *args, **kwargs):
    
    
    if request.method == 'POST':
        
        trabajo = request.GET.get('trabajo', '')
        bultos = request.GET.get('bultos', '')
        cliente = request.GET.get('cliente', '')
                    
        
        
        validar_global = trabajo
        
        global_en_base = GlobalPK.objects.filter(numero=validar_global)
        
        if not global_en_base:
            picking = GlobalPK(
                numero = trabajo,
                tipo = 'Ingreso por API',
                unidades = bultos,
                fecha_procesado = date.today(),
                hora_procesado = datetime.now().time(),
                estado_picking = 'Pendiente',
                estado_armado = 'Pendiente',
                creado_por = 'API',
                fecha_creacion = date.today(),
                nombre_planilla = cliente,
                en_picking = 'No',
                en_armado = 'No',

            )

            picking.save()
            
            
            
            
            return HttpResponse('Success')
        else:
            
            return HttpResponse('Trabajo Existente')
        
    else:
        return HttpResponse('Only POST')