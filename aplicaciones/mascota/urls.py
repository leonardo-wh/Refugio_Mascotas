from django.conf.urls import url, include

from aplicaciones.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

from django.conf import settings
from django.conf.urls.static import static

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
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


