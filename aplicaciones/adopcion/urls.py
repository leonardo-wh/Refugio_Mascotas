from django.conf.urls import url
from aplicaciones.adopcion.views import index_adopcion, solicitud_view, solicitud_list, solicitud_edit, solicitud_delete, \
    SolicitudList, SolicitudCreate, SolicitudDelete, SolicitudUpdate


urlpatterns = [
    url(r'^index$', index_adopcion),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'),

    url(r'^solicituddef/listar$', solicitud_list, name='solicitud_listardef'),
    url(r'^solicituddef/nueva$', solicitud_view, name='solicitud_creardef'),
    url(r'^solicituddef/editar/(?P<pk>\d+)$', solicitud_edit, name='solicitud_editardef'),
    url(r'^solicituddef/eliminar/(?P<pk>\d+)$', solicitud_delete, name='solicitud_eliminardef'),
]
