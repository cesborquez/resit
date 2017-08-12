from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from aplicaciones.pedido.models import Pedido
from aplicaciones.pedido.forms import PedidoForm


class PedidoList (ListView):
	model = Pedido
	template_name = 'pedido/pedido_list.html'
	ordering = ['fecha_pedido']
	paginate_by = 5

class PedidoCreate(CreateView):
	model = Pedido
	form_class = PedidoForm
	template_name = 'pedido/pedido_reg.html'
	success_url	 = reverse_lazy('pedido:pedido_listar')

class PedidoUpdate(UpdateView):
	model  = Pedido
	form_class = PedidoForm
	template_name = 'pedido/pedido_reg.html'
	success_url	 = reverse_lazy('pedido:pedido_listar')

class PedidoDelete(DeleteView):
	model  = Pedido
	success_url	 = reverse_lazy('pedido:pedido_listar')


