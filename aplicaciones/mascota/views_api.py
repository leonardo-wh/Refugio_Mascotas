from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404
from .views import ListMascota
from aplicaciones.mascota.forms import MascotaForm, Mascota
from aplicaciones.adopcion.forms import Solicitud, Persona
import json
from django.contrib.auth.decorators import permission_required


def list_warehouse(request):
    instance_api = ListMascota.as_view()(request)
    mascota = instance_api.data.serializer.instance
    # mascota = json.dumps(instance_api)
    contexto = {'mascotas': mascota}
    print(contexto)
    return render(request, 'mascota/mascota_list_api.html', contexto)
