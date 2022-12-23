from django.test import TestCase

# Create your tests here.

import xml
import json
# import requests

# url = "http://webservice.oca.com.ar/ePak_tracking/Oep_TrackEPak.asmx/GetEnvioEstadoActual?wsdl"
# envioNumero = "4737600000002528661"
# ordenRetiro = 0

# solicitud_xml = f"""
# <envioNumero>{envioNumero}</envioNumero>
# <ordenRetiro>{ordenRetiro}</ordenRetiro>
# """

# solicitud = requests.post(url,
#                           data=solicitud_xml,
#                           headers={'Content-Type':'application/xml'}
#                           )

import xmltodict
import requests

reqUrl = "http://webservice.oca.com.ar/ePak_tracking/Oep_TrackEPak.asmx/GetEnvioEstadoActual"
# http://webservice.oca.com.ar/ePak_tracking/Oep_TrackEPak.asmx/Tracking_Pieza?NroDocumentoCliente=2360068&CUIT=0&Pieza=0
numeroEnvio = "4737600000002528661"

ordenRetiro = 0
url = reqUrl + "?numeroEnvio=" + numeroEnvio + "&ordenRetiro="+ str(ordenRetiro)
headersList = {
    "Content-Type": "application/xml"
    }
payload = ''
response = requests.get(url, data=payload,  headers=headersList)
with response:
    xml_parsed = xmltodict.parse(response.text)

estado_pieza = xml_parsed['DataSet']['diffgr:diffgram']['NewDataSet']['Table']['Estado']
nro_guia = xml_parsed['DataSet']['diffgr:diffgram']['NewDataSet']['Table']['Remito']

print(estado_pieza)
print(nro_guia)





diccionario = {'DataSet': {'@xmlns': '#Oca_e_Pak', 'xs:schema':{'@id': 'NewDataSet',
                                                                '@xmlns': '',
                                                                '@xmlns:xs': 'http://www.w3.org/2001/XMLSchema',
                                                                '@xmlns:msdata': 'urn:schemas-microsoft-com:xml-msdata',
                                                                'xs:element': {
                                                                    '@name': 'NewDataSet',
                                                                    '@msdata:IsDataSet': 'true',
                                                                    '@msdata:Locale': '', 'xs:complexType': {
                                                                        'xs:choice': {
                                                                            '@minOccurs': '0',
                                                                            '@maxOccurs': 'unbounded',
                                                                            'xs:element': {
                                                                                '@name': 'Table', 
                                                                                'xs:complexType': {
                                                                                    'xs:sequence': {
                                                                                        'xs:element': [
                                                                                            {'@name': 'Operativa', '@type': 'xs:int', '@minOccurs': '0'}, 
                                                                                            {'@name': 'OrdenRetiro', '@type': 'xs:int', '@minOccurs': '0'},
                                                                                            {'@name': 'FechaRetiro', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'Remito', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'Destinatarios', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'eMail', '@type': 'xs:string', '@minOccurs': '0'}, 
                                                                                            {'@name': 'NumeroEnvio', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'CantidadPaquetes', '@type': 'xs:int', '@minOccurs': '0'},
                                                                                            {'@name': 'PesoTotal', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'PesoAforadoTotal', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'VolumenTotal', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'PrecioEnvio', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'Seguro', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'FechaImposicion', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'SucursalActual', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'CIDestino', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'FechaEstado', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'Estado', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'IdEstado', '@type': 'xs:int', '@minOccurs': '0'},
                                                                                            {'@name': 'Motivo', '@type': 'xs:string', '@minOccurs': '0'},
                                                                                            {'@name': 'Alto', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'Ancho', '@type': 'xs:decimal', '@minOccurs': '0'},
                                                                                            {'@name': 'Largo', '@type': 'xs:decimal', '@minOccurs': '0'}
                                                                                            ]
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                'diffgr:diffgram': {
                                                                    '@xmlns:msdata': 'urn:schemas-microsoft-com:xml-msdata',
                                                                    '@xmlns:diffgr': 'urn:schemas-microsoft-com:xml-diffgram-v1',
                                                                    'NewDataSet': {
                                                                        '@xmlns': '', 
                                                                        'Table': {
                                                                            '@diffgr:id': 'Table1',
                                                                            '@msdata:rowOrder': '0',
                                                                            'Operativa': '308518',
                                                                            'OrdenRetiro': '103051868',
                                                                            'FechaRetiro': '22/12/2022',
                                                                            'Remito': '2600797',
                                                                            'Destinatarios': 'SANTIEUSANIO EDUARDO ADRI',
                                                                            'eMail': 'TALLERADRISAN@GMAIL.COM',
                                                                            'NumeroEnvio': '4737600000002528661',
                                                                            'CantidadPaquetes': '1',
                                                                            'Seguro': '0.0000',
                                                                            'SucursalActual': 'TRÁFICO',
                                                                            'CIDestino': None,
                                                                            'FechaEstado': '21/12/2022',
                                                                            'Estado': 'En proceso de Retiro',
                                                                            'IdEstado': '1', 
                                                                            'Motivo': 'Sin Motivo'}
                                                                        }
                                                                    }
                                                                }
                           }
               }






















# estado_pieza = xml_parsed

# print(estado_pieza)
# if response.status_code == 200:
#     respuesta = response.encoding
#     print(respuesta)


# from urllib.request import urlopen
# from xml.etree.ElementTree import parse


# solicitud = urlopen(url)

# doc_xml = parse(solicitud)

# for parametro in doc_xml.iterfind('channel/item'):
#     print(parametro)
#     estado = parametro.findtext('<Estado>')
#     print(estado)
    




