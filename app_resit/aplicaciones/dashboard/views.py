from django.shortcuts import render, redirect
from django.http import HttpResponse
from aplicaciones.stock.models import Stock
from aplicaciones.logistica.models import Logistica


# Create your views here.

def stock_list(request):
	stock = Stock.objects.all()
	contexto = {'stocks':stock}
	return render(request, 'dashboard/dashboard_list.html',contexto)

def logistica_list(request):
	logistica = Logistica.objects.all()
	contexto = {'logisticas':logistica}
	return render(request, 'dashboard/dashboard_list.html',contexto)
