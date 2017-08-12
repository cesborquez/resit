from django.shortcuts import render
from aplicaciones.stock.models import Stock
from django.views.generic import ListView

class StockList (ListView):
	model = Stock
	template_name = 'stock/producto_list.html'
