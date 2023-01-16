from django.test import TestCase
from django.http import HttpResponse, JsonResponse
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()



def enviarCorreo():
    

    mensaje = 'Hola, mira como mando mails desde python jejej'
    correo_electronico = 'cpiran@southpost.com.ar'
    asunto = 'Yo mando mails dsd python'

    body = 'Subject: {}\n\n{}'.format(asunto, mensaje)
    server = smtplib.SMTP('smtp.office365.com','587')
    server.starttls()
    server.login(os.getenv('EMAIL_HOST_USER'),os.getenv('EMAIL_HOST_PASSWORD'))
    server.sendmail('santiagonavalon@southpost.com.ar', correo_electronico, body)
    server.quit()
    #iybifjubgmdxzkos -- contraseña de terceros de google

    
    
enviarCorreo()