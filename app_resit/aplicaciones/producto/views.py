from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from aplicaciones.producto.models import Producto
from aplicaciones.producto.forms import ProductoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ProductoList (ListView):
	model = Producto
	template_name = 'producto/producto_list.html'
	ordering = ['id_prod']
	paginate_by = 3



class ProductoCreate(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_reg.html'
	success_url	 = reverse_lazy('producto:producto_listar')

class ProductoUpdate(UpdateView):
	model  = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_reg.html'
	success_url	 = reverse_lazy('producto:producto_listar')

class ProductoDelete(DeleteView):
	model  = Producto
	success_url	 = reverse_lazy('producto:producto_listar')









#class ProductoDelete(DeleteView):
#	model  = Producto
#	success_url	 = reverse_lazy('producto:producto_listar')