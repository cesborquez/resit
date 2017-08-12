from __future__ import absolute_import
from django.conf.urls import url, include

from aplicaciones.logistica.views import LogisticaList, LogisticaCreate, LogisticaUpdate, LogisticaDelete

urlpatterns = [
		
	  url(r'^nuevo$', LogisticaCreate.as_view(), name ='logistica_crear'),  
      url(r'^$', LogisticaList.as_view(), name ='logistica_listar'),
      url(r'^listar$', LogisticaList.as_view(), name ='logistica_listar'),

      url(r'^editar/(?P<pk>\w+)/$', LogisticaUpdate.as_view(), name ='logistica_editar'),
      url(r'^eliminar/(?P<pk>\w+)/$', LogisticaDelete.as_view(), name ='logistica_eliminar'),
      



    ]