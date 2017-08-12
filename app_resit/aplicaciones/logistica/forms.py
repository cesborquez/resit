from django import forms

from aplicaciones.logistica.models import Logistica



class LogisticaForm(forms.ModelForm):
	class Meta:
		model = Logistica

		fields =[
		'patente',
		'vehiculo',
		'conductor',

		]

		labels = {

		'patente'	:'Patente del Vehiculo',
		'vehiculo'	:'Marca del Vehiculo',
		'conductor'	:'Nombre Conductor',

		}

		widgets = {
		'patente'	: forms.TextInput(attrs={'class':'form-control'}),
		'vehiculo'	: forms.TextInput(attrs={'class':'form-control'}),
		'conductor'	: forms.TextInput(attrs={'class':'form-control'}),

		}
