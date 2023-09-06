from django.conf.urls import url, include

from aplicaciones.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, \
    ListMascota, DetailPersona, list_mascota, detail_persona, ListMascotaGeneric, DetailMascotaGeneric, \
    ListMascotaView, DetailPersonaGeneric

from .views_api import list_mascotas, edit_mascotas, delete_mascotas, list_mascotas_apiview, edit_mascotas_apiview, \
    delete_mascotas_apiview, list_mascotas_generic, edit_mascotas_generic, delete_mascotas_generic, \
    list_mascotas_viewset, edit_mascotas_viewset, delete_mascotas_viewset, create_mascotas, create_mascotas_apiview, \
    create_mascotas_generic, create_mascotas_viewset

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
    url(r'^mascotadef/nuevo$', mascota_view, name='mascota_creardef'),
    url(r'^mascotadef/listar$', mascota_list, name='mascota_listardef'),
    url(r'^mascotadef/editar/(?P<pk>\d+)$', mascota_edit, name='mascota_editardef'),
    url(r'^mascotadef/eliminar/(?P<pk>\d+)$', mascota_delete, name='mascota_eliminardef'),

    # APIView
    url(r'^mascotas/$', ListMascota.as_view(), name='lista-mascota'),
    url(r'^mascotas/(?P<pk>\d+)/persona$', DetailPersona.as_view(), name='detail-persona'),

    # @api_view
    url(r'^mascotas_apiview/$', list_mascota, name='lista-mascota_apiview'),
    url(r'^mascotas_apiview/(?P<pk>\d+)/persona$', detail_persona, name='detail-persona_apiview'),

    # Generic ApiView
    url(r'^mascotas_generic/$', ListMascotaGeneric.as_view(), name='lista-mascota_generic'),
    url(r'^mascotas_generic/(?P<pk>\d+)/persona$', DetailPersonaGeneric.as_view(), name='detail-mascota_generic'),



    url(r'^mascotas_view/listar$', list_mascotas, name='mascota_listar_api'),
    url(r'^mascotas_view/crear$', create_mascotas, name='mascota_crear_api'),
    url(r'^mascotas_view/editar/(?P<pk>\d+)$', edit_mascotas, name='mascota_editar_api'),
    url(r'^mascotas_view/eliminar/(?P<pk>\d+)$', delete_mascotas, name='mascota_eliminar_api'),

    url(r'^mascotas_apiview/listar$', list_mascotas_apiview, name='mascota_listar_apiview'),
    url(r'^mascotas_apiview/crear$', create_mascotas_apiview, name='mascota_crear_apiview'),
    url(r'^mascotas_apiview/editar/(?P<pk>\d+)$', edit_mascotas_apiview, name='mascota_editar_apiview'),
    url(r'^mascotas_apiview/eliminar/(?P<pk>\d+)$', delete_mascotas_apiview, name='mascota_eliminar_apiview'),

    url(r'^mascotas_generic/listar$', list_mascotas_generic, name='mascota_listar_generic'),
    url(r'^mascotas_generic/crear$', create_mascotas_generic, name='mascota_crear_generic'),
    url(r'^mascotas_generic/editar/(?P<pk>\d+)$', edit_mascotas_generic, name='mascota_editar_generic'),
    url(r'^mascotas_generic/eliminar/(?P<pk>\d+)$', delete_mascotas_generic, name='mascota_eliminar_generic'),

    url(r'^mascotas_viewset/listar$', list_mascotas_viewset, name='mascota_listar_viewset'),
    url(r'^mascotas_viewset/crear$', create_mascotas_viewset, name='mascota_crear_viewset'),
    url(r'^mascotas_viewset/editar/(?P<pk>\d+)$', edit_mascotas_viewset, name='mascota_editar_viewset'),
    url(r'^mascotas_viewset/eliminar/(?P<pk>\d+)$', delete_mascotas_viewset, name='mascota_eliminar_viewset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
