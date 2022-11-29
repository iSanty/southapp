from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import InformePreparacion


        
        
class PlanillaPKSerializer(serializers.ModelSerializer):
    class Meta:
        Model = InformePreparacion
        exclude = ['is_removed', 'created', 'modified']
        