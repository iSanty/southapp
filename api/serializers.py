from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Guia


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = ('id','nro_guia', 'remito')