# Create your views here.


from rest_framework import status
from .serializers import  PlanillaPKSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InformePreparacion
from django.http import Http404
    

    
class PostPlanillaPK(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        
        globales = InformePreparacion.objects.all()
        serializer = PlanillaPKSerializer(globales, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PlanillaPKSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PostPlanillaPK_Detail(APIView):
    
    def get_object(self, pk):
        try:
            return InformePreparacion.objects.get(pk=pk)
        except InformePreparacion.DoesNotExist:
            raise Http404
        
        
    def get(self, request, pk, format=None):
        globales = self.get_object(pk)
        serializer = PlanillaPKSerializer(globales)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        globales = self.get_object(pk)
        serializer = PlanillaPKSerializer(globales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        globales = self.get_object(pk)
        globales.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        