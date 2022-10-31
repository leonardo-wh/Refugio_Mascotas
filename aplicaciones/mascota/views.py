from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404

from aplicaciones.mascota.forms import MascotaForm, Mascota
from aplicaciones.adopcion.forms import Solicitud, Persona

from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import MascotaSerializer, PersonaSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.


def index(request):
    return render(request, 'mascota/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listardef')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    print (contexto)
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, pk):
    mascota = Mascota.objects.get(id=pk)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listardef')
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_delete(request, pk):
    mascota = Mascota.objects.get(id=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listardef')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')


# View usando APIView
class ListMascota(APIView):

    def get(self, request):
        mascotas = Mascota.objects.all()
        mascota_json = MascotaSerializer(mascotas, many=True)
        return Response(mascota_json.data)

    def post(self, request):
        mascota_json = MascotaSerializer(data=request.data)  # UnMarshall
        if mascota_json.is_valid():
            mascota_json.save()
            return Response(mascota_json.data, status=201)
        return Response(mascota_json.errors, status=400)


class DetailMascota(APIView):
    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mascota = self.get_object(pk)
        mascota_json = MascotaSerializer(mascota)
        return Response(mascota_json.data)

    def put(self, request, pk):
        mascota = self.get_object(pk)
        mascota_json = MascotaSerializer(mascota, data=request.data)
        if mascota_json.is_valid():
            mascota_json.save()
            return Response(mascota_json.data)
        return Response(mascota_json.errors, status=400)

    def delete(self, request, pk):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=204)


class DetailPersona(APIView):
    def get_object(self, pk):
        try:
            query = Mascota.objects.get(pk=pk)
            return query.persona
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        persona = self.get_object(pk)
        persona_json = PersonaSerializer(persona)
        return Response(persona_json.data)

    def put(self, request, pk):
        persona = self.get_object(pk)
        persona_json = PersonaSerializer(persona, data=request.data)
        if persona_json.is_valid():
            persona_json.save()
            return Response(persona_json.data)
        return Response(persona_json.errors, status=400)

    def delete(self, request, pk):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=204)


# View usando @api_view
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def list_mascota(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        mascota_json = MascotaSerializer(mascotas, many=True)
        return Response(mascota_json.data)

    if request.method == 'POST':
        mascota_json = MascotaSerializer(data=request.data)  # UnMarshall
        if mascota_json.is_valid():
            mascota_json.save()
            return Response(mascota_json.data, status=201)
        return Response(mascota_json.errors, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def detail_mascota(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        mascota_json = MascotaSerializer(mascota)
        return Response(mascota_json.data)

    if request.method == 'PUT':
        mascota_json = MascotaSerializer(mascota, data=request.data)
        if mascota_json.is_valid():
            mascota_json.save()
            return Response(mascota_json.data)
        return Response(mascota_json.errors, status=400)

    if request.method == 'DELETE':
        mascota.delete()
        return Response(status=204)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def detail_persona(request, pk):
    try:
        query = Mascota.objects.get(pk=pk)
        persona = query.persona
    except Mascota.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        persona_json = PersonaSerializer(persona)
        return Response(persona_json.data)

    if request.method == 'PUT':
        persona_json = PersonaSerializer(persona, data=request.data)
        if persona_json.is_valid():
            persona_json.save()
            return Response(persona_json.data)
        return Response(persona_json.errors, status=400)

    if request.method == 'DELETE':
        persona.delete()
        return Response(status=204)


# View usando Generic ApiView
class ListMascotaGeneric(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DetailMascotaGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class DetailPersonaGeneric(GenericAPIView, RetrieveModelMixin):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def get(self, request, **kwargs):
        mascota_instance = self.get_object()
        queryset = mascota_instance.persona
        serializer = PersonaSerializer(queryset)
        return Response(serializer.data)


# View usando Generic ViewSet
class ListMascotaView(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    @action(methods=['GET'], detail=True, url_path='persona')
    def list_services(self, request, pk):
        mascota_instance = self.get_object()
        queryset = mascota_instance.persona
        serializer = PersonaSerializer(queryset)
        return Response(serializer.data)
