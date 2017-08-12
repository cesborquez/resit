from __future__ import absolute_import
from django.conf.urls import url, include

from aplicaciones.producto.views import ProductoList, ProductoCreate , ProductoUpdate, ProductoDelete

urlpatterns = [
# url(r'^$', index, name='index'), 
      #url(r'^$', cliente_list, name ='cliente_listar'),
      #url(r'^nuevo$', cliente_view, name ='cliente_crear'),
      url(r'^nuevo$', ProductoCreate.as_view(), name ='producto_crear'),
      url(r'^$', ProductoList.as_view(), name ='producto_listar'),
      url(r'^listar$', ProductoList.as_view(), name ='producto_listar'),
#      url(r'^$', StockList.as_view(), name ='pedido_listar'),
 #     url(r'^listar$', StockList.as_view(), name ='pedido_listar'),
      url(r'^editar/(?P<pk>\d+)/$', ProductoUpdate.as_view(), name ='producto_editar'),
      url(r'^eliminar/(?P<pk>\d+)/$', ProductoDelete.as_view(), name ='producto_eliminar'),
      #url(r'^eliminar/(?P<id_prod>\d+)/$', ProductoDelete.as_view(), name ='producto_eliminar'),




    ]