from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from aplicaciones.cliente.forms import ClienteForm
from aplicaciones.cliente.models import Cliente

# Create your views here.

class ClienteCreate(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_reg.html'
	success_url	 = reverse_lazy('cliente:cliente_listar')

class ClienteList (ListView):
	model = Cliente
	template_name = 'cliente/cliente_list.html'
	paginate_by = 3
	#ordering = ['estado']

class ClienteUpdate(UpdateView):
	model  = Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_reg.html'
	success_url	 = reverse_lazy('cliente:cliente_listar')

class ClienteDelete(DeleteView):
	model  = Cliente
	success_url	 = reverse_lazy('cliente:cliente_listar')










#def index(request):
#	return render(request ,'cliente/index.html')

# def cliente_view(request):
# 	if request.method == 'POST':
# 		form = ClienteForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('cliente:cliente_listar')

# 	else:
# 		form = ClienteForm()

# 	return render(request, 'cliente/cliente_reg.html',{'form':form})


# def cliente_list(request):
# 	cliente 	= Cliente.objects.all().order_by('cod_cliente')
# 	contexto 	= {'clientes':cliente}
# 	paginate_by = 3
# 	return render (request, 'cliente/cliente_list.html', contexto)


# def cliente_edit(request, cod_cliente):
# 	cliente =  Cliente.objects.get(cod_cliente=cod_cliente)
# 	if request.method == 'GET':
# 		form = ClienteForm(instance=cliente)
# 	else:
# 		form = ClienteForm(request.POST, instance=cliente)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('cliente:cliente_listar')
# 	return render(request,'cliente/cliente_reg.html',{'form':form})


# def cliente_delete(request,cod_cliente):
# 	cliente = Cliente.objects.get(cod_cliente=cod_cliente)
# 	if request.method == 'POST':
# 		cliente.delete()
# 		return redirect('cliente:cliente_listar')
# 	return render(request,'cliente/cliente_delete.html',{'cliente':cliente})


# class ClienteCreate (CreateView):

# 	model 			= Cliente
# 	form_class 		= ClienteForm
# 	template_name 	= 'cliente/cliente_reg.html'
# 	success_url 	= reverse_lazy('cliente:cliente_listar')
