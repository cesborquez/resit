
from django.conf.urls import handler404,handler500
from django.conf.urls import url, include
from django.contrib import admin
from app_resit import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('aplicaciones.pedido.urls', namespace="pedido")),
    url(r'^cliente/', include('aplicaciones.cliente.urls', namespace="cliente")),
    url(r'^logistica/', include('aplicaciones.logistica.urls', namespace="logistica")),
    url(r'^producto/', include('aplicaciones.producto.urls', namespace="producto")),
    url(r'^pedido/', include('aplicaciones.pedido.urls', namespace="pedido2")),
    url(r'^stock/', include('aplicaciones.stock.urls', namespace="stock")),
    url(r'^dashboard/', include('aplicaciones.dashboard.urls', namespace="dashboard")),
]

handler404 = 'views.custom_404'
handler500 = 'views.custom_500'