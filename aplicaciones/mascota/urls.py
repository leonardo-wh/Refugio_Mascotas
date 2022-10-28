from django.conf.urls import url, include

from aplicaciones.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, \
    ListMascota, DetailMascota, list_mascota, detail_mascota, ListMascotaGeneric, DetailMascotaGeneric, \
    ListMascotaView

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(
    'mascotas_view', ListMascotaView, basename='lista-mascota_view'
)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^mascota/nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^mascota/listar$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^mascota/editar/(?P<pk>\d+)$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^mascota/eliminar/(?P<pk>\d+)$', MascotaDelete.as_view(), name='mascota_eliminar'),

    # APIView
    url(r'^mascotas/$', ListMascota.as_view(), name='lista-mascota'),
    url(r'^mascotas/(?P<pk>\d+)/persona$', DetailMascota.as_view(), name='detail-mascota'),

    # @api_view
    url(r'^mascotas_apiview/$', list_mascota, name='lista-mascota_apiview'),
    url(r'^mascotas_apiview/(?P<pk>\d+)/persona$', detail_mascota, name='detail-mascota_apiview'),

    # Generic ApiView
    url(r'^mascotas_generic/$', ListMascotaGeneric.as_view(), name='lista-mascota_generic'),
    url(r'^mascotas_generic/(?P<pk>\d+)/persona$', DetailMascotaGeneric.as_view(), name='detail-mascota_generic'),

    url(r'^mascotadef/nuevo$', mascota_view, name='mascota_creardef'),
    url(r'^mascotadef/listar$', mascota_list, name='mascota_listardef'),
    url(r'^mascotadef/editar/(?P<pk>\d+)$', mascota_edit, name='mascota_editardef'),
    url(r'^mascotadef/eliminar/(?P<pk>\d+)$', mascota_delete, name='mascota_eliminardef'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
