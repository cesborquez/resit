from django import forms

from aplicaciones.producto.models import Producto



class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields =[
		'nombre',
	

		]

		labels = {

		'nombre':'Nombre',


		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
	


		}
