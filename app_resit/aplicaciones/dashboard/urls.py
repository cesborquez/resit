from __future__ import absolute_import
from django.conf.urls import url, include

from aplicaciones.dashboard.views import stock_list,logistica_list

urlpatterns = [

    #  url(r'^$', ProductoList.as_view(), name ='producto_listar'),
      url(r'^$', stock_list,  name ='dashboard_stock'),
      url(r'^$', logistica_list, name ='dashboard_logistica'),



    ]