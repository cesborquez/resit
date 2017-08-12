from __future__ import absolute_import
from django.conf.urls import url, include

from aplicaciones.cliente.views import ClienteList,ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
		
	  url(r'^nuevo$', ClienteCreate.as_view(), name ='cliente_crear'),  
      url(r'^$', ClienteList.as_view(), name ='cliente_listar'),
      url(r'^listar$', ClienteList.as_view(), name ='cliente_listar'),

      url(r'^editar/(?P<pk>\w+)/$', ClienteUpdate.as_view(), name ='cliente_editar'),
      url(r'^eliminar/(?P<pk>\w+)/$', ClienteDelete.as_view(), name ='cliente_eliminar'),
      



    ]