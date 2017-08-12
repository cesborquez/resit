from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from aplicaciones.logistica.models import Logistica
from aplicaciones.logistica.forms import LogisticaForm




class LogisticaCreate(CreateView):
	model = Logistica
	form_class = LogisticaForm
	template_name = 'logistica/logistica_reg.html'
	success_url	 = reverse_lazy('logistica:logistica_listar')

class LogisticaList (ListView):
	model = Logistica
	template_name = 'logistica/logistica_list.html'
	paginate_by = 3
	#ordering = ['estado']

class LogisticaUpdate(UpdateView):
	model  = Logistica
	form_class = LogisticaForm
	template_name = 'logistica/logistica_reg.html'
	success_url	 = reverse_lazy('logistica:logistica_listar')

class LogisticaDelete(DeleteView):
	model  = Logistica
	success_url	 = reverse_lazy('logistica:logistica_listar')










