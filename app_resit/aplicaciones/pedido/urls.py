from __future__ import absolute_import
from django.conf.urls import url, include

from aplicaciones.pedido.views import PedidoCreate, PedidoList, PedidoUpdate , PedidoDelete

urlpatterns = [

    	url(r'^nuevo$', PedidoCreate.as_view(), name ='pedido_crear'),
      	url(r'^$', PedidoList.as_view(), name ='pedido_listar'),
      	url(r'^listar$', PedidoList.as_view(), name ='pedido_listar'),


      url(r'^editar/(?P<pk>\d+)/$', PedidoUpdate.as_view(), name ='pedido_editar'),
      url(r'^eliminar/(?P<pk>\d+)/$', PedidoDelete.as_view(), name ='pedido_eliminar'),
   


    ]