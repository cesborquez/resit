from django import forms

from aplicaciones.cliente.models import Cliente



class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

		fields =[
		'nombre',
		'direccion',
		'comuna',
		'tiempo_recorrido',

		]

		labels = {

		'nombre': 'Cliente (Local Comercial)',
		'direccion':'Dirección',
		'comuna': 'Comuna',
		'tiempo_recorrido':'Tiempo de Recorrido',

		}

		widgets = {

		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'direccion': forms.TextInput(attrs={'class':'form-control'}),
		'comuna': forms.TextInput(attrs={'class':'form-control'}),
		'tiempo_recorrido':forms.TextInput(attrs={'class':'form-control'}),

		}
