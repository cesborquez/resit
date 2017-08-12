from __future__ import absolute_import
from django.conf.urls import url, include

from aplicaciones.stock.views import  StockList

urlpatterns = [

   
      url(r'^$', StockList.as_view(), name ='stock_listar'),
      url(r'^listar$', StockList.as_view(), name ='stock_listar'),
     



    ]