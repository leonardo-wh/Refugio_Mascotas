from django.shortcuts import render, redirect, reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404
from .views import ListMascota, DetailMascota, list_mascota, detail_mascota, ListMascotaGeneric, DetailMascotaGeneric, \
    ListMascotaView
from aplicaciones.mascota.forms import MascotaForm, Mascota
from rest_framework import status
from django.contrib import messages
from aplicaciones.adopcion.forms import Solicitud, Persona
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required


# APIView
def list_mascotas(request):
    instance_api = ListMascota.as_view()(request)
    mascota = instance_api.data.serializer.instance
    if instance_api.status_code == status.HTTP_200_OK:
        # mascota = json.dumps(instance_api)
        contexto = {'mascotas': mascota}
        return render(request, 'mascota/mascota_list_api.html', contexto)
    else:
        serializers_errors = instance_api.data.serializer.errors
        for error in serializers_errors:
            if error == 'non_field_errors':
                instance_api.add_error('__all__', serializers_errors.get(error)[0])
            else:
                instance_api.add_error(error, serializers_errors.get(error)[0])


def edit_mascotas(request, pk):
    if request.method == 'POST':
        request.method = 'GET'
        object = DetailMascota.as_view()(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_api"))
        object = object.data.serializer.instance
        form = MascotaForm(request.POST, instance=object)

        if form.is_valid():
            request.method = "PUT"
            object_instance = DetailMascota.as_view()(request=request, pk=pk)
            if object_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se edito correctamente la mascota.")
            else:
                serializer_errors = object_instance.data.serializer.errors
                for error in serializer_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializer_errors.get(error)[0])
                    else:
                        form.add_error(error, serializer_errors.get(error)[0])
    else:
        object = DetailMascota.as_view()(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_api"))
        object = object.data.serializer.instance
        form = MascotaForm(instance=object)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def delete_mascotas(request, pk):
    if request.method == "POST":
        request.method = "GET"
        object = DetailMascota.as_view()(request=request, pk=pk)
        if object.status_code != status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_api"))

        request.method = "DELETE"
        instance = DetailMascota.as_view()(request=request, pk=pk)
        if instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota")
        else:
            messages.error(request, "No se pudo Eliminar la mascota")
        return HttpResponseRedirect(reverse("mascota_listar_api"))
    else:
        product_instance = DetailMascota.as_view()(request=request, pk=pk)
        if not product_instance.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_api"))
        detail_product = product_instance.data
    return render(request, 'mascota/mascota_delete.html', detail_product)


def create_mascotas(request):
    form = MascotaForm()
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            instance = ListMascota.as_view()(request=request)
            if instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Mascota creada correctamente")
                return HttpResponseRedirect(reverse('mascota_listar_api'))
            else:
                serializers_errors = instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    return render(request, 'mascota/mascota_form.html', {'form': form})


# @apiview
def list_mascotas_apiview(request):
    instance_api = list_mascota(request)
    mascota = instance_api.data.serializer.instance
    if instance_api.status_code == status.HTTP_200_OK:
        # mascota = json.dumps(instance_api)
        contexto = {'mascotas': mascota}
        return render(request, 'mascota/mascota_list_apiview.html', contexto)
    else:
        serializers_errors = instance_api.data.serializer.errors
        for error in serializers_errors:
            if error == 'non_field_errors':
                instance_api.add_error('__all__', serializers_errors.get(error)[0])
            else:
                instance_api.add_error(error, serializers_errors.get(error)[0])


def edit_mascotas_apiview(request, pk):
    if request.method == 'POST':
        request.method = 'GET'
        object = detail_mascota(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_apiview"))
        object = object.data.serializer.instance
        form = MascotaForm(request.POST, instance=object)

        if form.is_valid():
            request.method = "PUT"
            object_instance = detail_mascota(request=request, pk=pk)
            if object_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se edito correctamente la mascota.")
            else:
                serializer_errors = object_instance.data.serializer.errors
                for error in serializer_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializer_errors.get(error)[0])
                    else:
                        form.add_error(error, serializer_errors.get(error)[0])
    else:
        object = detail_mascota(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_apiview"))
        object = object.data.serializer.instance
        form = MascotaForm(instance=object)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def delete_mascotas_apiview(request, pk):
    if request.method == "POST":
        request.method = "GET"
        object = detail_mascota(request=request, pk=pk)
        if object.status_code != status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_apiview"))

        request.method = "DELETE"
        instance = detail_mascota(request=request, pk=pk)
        if instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota")
        else:
            messages.error(request, "No se pudo Eliminar la mascota")
        return HttpResponseRedirect(reverse("mascota_listar_apiview"))
    else:
        product_instance = detail_mascota(request=request, pk=pk)
        if not product_instance.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_apiview"))
        detail_product = product_instance.data
    return render(request, 'mascota/mascota_delete.html', detail_product)


def create_mascotas_apiview(request):
    form = MascotaForm()
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            instance = list_mascota(request=request)
            if instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Mascota creada correctamente")
                return HttpResponseRedirect(reverse('mascota_listar_apiview'))
            else:
                serializers_errors = instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    return render(request, 'mascota/mascota_form.html', {'form': form})


# Generic view
def list_mascotas_generic(request):
    instance_api = ListMascotaGeneric.as_view()(request)
    mascota = instance_api.data.serializer.instance
    if instance_api.status_code == status.HTTP_200_OK:
        # mascota = json.dumps(instance_api)
        contexto = {'mascotas': mascota}
        return render(request, 'mascota/mascota_list_generic.html', contexto)
    else:
        serializers_errors = instance_api.data.serializer.errors
        for error in serializers_errors:
            if error == 'non_field_errors':
                instance_api.add_error('__all__', serializers_errors.get(error)[0])
            else:
                instance_api.add_error(error, serializers_errors.get(error)[0])


def edit_mascotas_generic(request, pk):
    if request.method == 'POST':
        request.method = 'GET'
        object = DetailMascotaGeneric.as_view()(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_generic"))
        object = object.data.serializer.instance
        form = MascotaForm(request.POST, instance=object)

        if form.is_valid():
            request.method = "PUT"
            object_instance = DetailMascotaGeneric.as_view()(request=request, pk=pk)
            if object_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se edito correctamente la mascota.")
            else:
                serializer_errors = object_instance.data.serializer.errors
                for error in serializer_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializer_errors.get(error)[0])
                    else:
                        form.add_error(error, serializer_errors.get(error)[0])
    else:
        object = DetailMascotaGeneric.as_view()(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_generic"))
        object = object.data.serializer.instance
        form = MascotaForm(instance=object)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def delete_mascotas_generic(request, pk):
    if request.method == "POST":
        request.method = "GET"
        object = DetailMascotaGeneric.as_view()(request=request, pk=pk)
        if object.status_code != status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_generic"))

        request.method = "DELETE"
        instance = DetailMascotaGeneric.as_view()(request=request, pk=pk)
        if instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota")
        else:
            messages.error(request, "No se pudo Eliminar la mascota")
        return HttpResponseRedirect(reverse("mascota_listar_generic"))
    else:
        product_instance = DetailMascotaGeneric.as_view()(request=request, pk=pk)
        if not product_instance.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_generic"))
        detail_product = product_instance.data
    return render(request, 'mascota/mascota_delete.html', detail_product)


def create_mascotas_generic(request):
    form = MascotaForm()
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            instance = ListMascotaGeneric.as_view()(request=request)
            if instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Mascota creada correctamente")
                return HttpResponseRedirect(reverse('mascota_listar_generic'))
            else:
                serializers_errors = instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    return render(request, 'mascota/mascota_form.html', {'form': form})


# Viewsets
def list_mascotas_viewset(request):
    instance_api = ListMascotaView.as_view({'get': 'list'})(request)
    mascota = instance_api.data.serializer.instance
    if instance_api.status_code == status.HTTP_200_OK:
        # mascota = json.dumps(instance_api)
        contexto = {'mascotas': mascota}
        return render(request, 'mascota/mascota_list_viewset.html', contexto)
    else:
        serializers_errors = instance_api.data.serializer.errors
        for error in serializers_errors:
            if error == 'non_field_errors':
                instance_api.add_error('__all__', serializers_errors.get(error)[0])
            else:
                instance_api.add_error(error, serializers_errors.get(error)[0])


def edit_mascotas_viewset(request, pk):
    if request.method == 'POST':
        request.method = 'GET'
        object = ListMascotaView.as_view({'get': 'list'})(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_viewset"))
        object = object.data.serializer.instance
        form = MascotaForm(request.POST)

        if form.is_valid():
            request.method = "PATCH"
            object_instance = ListMascotaView.as_view({'patch': 'partial_update'})(request=request, pk=pk)
            if object_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se edito correctamente la mascota.")
            else:
                serializer_errors = object_instance.data.serializer.errors
                for error in serializer_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializer_errors.get(error)[0])
                    else:
                        form.add_error(error, serializer_errors.get(error)[0])
    else:
        object = ListMascotaView.as_view({'get': 'retrieve'})(request=request, pk=pk)
        if not object.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_viewset"))
        object = object.data.serializer.instance
        form = MascotaForm(instance=object)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def delete_mascotas_viewset(request, pk):
    if request.method == "POST":
        request.method = "GET"
        object = ListMascotaView.as_view({'get': 'retrieve'})(request=request, pk=pk)
        if object.status_code != status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_viewset"))

        request.method = "DELETE"
        instance = ListMascotaView.as_view({'delete': 'destroy'})(request=request, pk=pk)
        if instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota")
        else:
            messages.error(request, "No se pudo Eliminar la mascota")
        return HttpResponseRedirect(reverse("mascota_listar_viewset"))
    else:
        instance = ListMascotaView.as_view({'get': 'retrieve'})(request=request, pk=pk)
        if not instance.status_code == status.HTTP_200_OK:
            messages.error(request, "No existe esta mascota")
            return HttpResponseRedirect(reverse("mascota_listar_viewset"))
        detail_product = instance.data
    return render(request, 'mascota/mascota_delete.html', detail_product)


def create_mascotas_viewset(request):
    form = MascotaForm()
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            instance = ListMascotaView.as_view({'post': 'create'})(request=request)
            if instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Mascota creada correctamente")
                return HttpResponseRedirect(reverse('mascota_listar_viewset'))
            else:
                serializers_errors = instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    return render(request, 'mascota/mascota_form.html', {'form': form})