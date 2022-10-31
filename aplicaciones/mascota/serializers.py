from rest_framework import serializers

from .models import Mascota
from aplicaciones.adopcion.models import Solicitud, Persona


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = (
            'id',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
        )


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
