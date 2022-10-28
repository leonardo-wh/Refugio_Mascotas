from rest_framework import serializers

from .models import Mascota
from aplicaciones.adopcion.models import Solicitud, Persona


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = (
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
            'imagen'
        )


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
