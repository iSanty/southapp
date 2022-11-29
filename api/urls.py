from django.urls import path


from .views import *

app_name = 'api'


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', PostPlanillaPK.as_view()),
    path('v1/informe_preparacion',  PostPlanillaPK.as_view()),
    path('v1/informe_preparacion_detalle/<int:pk>/',  PostPlanillaPK_Detail.as_view()),
    
]
