from django import forms

from aplicaciones.pedido.models import Pedido




class PedidoForm(forms.ModelForm):
	class Meta:
		model = Pedido

		fields =[
		'Cliente',
		'Producto',
		'cantidad',

	

		]

		labels = {

		'Cliente':'Cliente',
		'Producto':'Producto',
		'cantidad':'cantidad',


		}

		widgets = {
		'Cliente': forms.Select(attrs={'class':'form-control'}),
		'Producto': forms.Select(attrs={'class':'form-control'}),
		'cantidad': forms.TextInput(attrs={'class':'form-control'}),
	

		}
