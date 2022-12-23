import requests
import xmltodict

from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('api_token')

def solicitud_presis(consulta):
    nro_guia = consulta
    
    url = "http://epresis.southpost.com.ar/api/v2/seguimiento.json"
    
    
    auth_data = {'api_token':token, 'remito':'','nro_guia':nro_guia}

    respuesta = requests.post(url, data=auth_data)

    respuesta = respuesta.json()
    
    
    estado = respuesta['guia']['fechas'][0]
    
    return estado


    
def solicitud_oca(numeroEnvio):
    prefijo = '473760000000'
    numeroEnvio = numeroEnvio
    
    consulta = prefijo + numeroEnvio
    
    url = "http://webservice.oca.com.ar/ePak_tracking/Oep_TrackEPak.asmx/GetEnvioEstadoActual?numeroEnvio="+ consulta + "&ordenRetiro=0"
    
    headersList = {
    "Content-Type": "application/xml"
    }
    payload = ''
    response = requests.get(url, data=payload,  headers=headersList)
    
        
    with response:
        xml_parsed = xmltodict.parse(response.text)
        
        if xml_parsed:

            estado_pieza = xml_parsed['DataSet']['diffgr:diffgram']['NewDataSet']['Table']['Estado']
            nro_guia = xml_parsed['DataSet']['diffgr:diffgram']['NewDataSet']['Table']['Remito']
        
        
        
            lista = []
            lista.append(estado_pieza)
            lista.append(nro_guia)
            return lista
        else:
            return 'Error'
    
    