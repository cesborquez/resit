from django.db import models





class Cliente (models.Model):
	cod_cliente			= models.AutoField(primary_key=True)
	nombre				= models.CharField(max_length=50)
	direccion 			= models.CharField(max_length=50)
	comuna				= models.CharField(max_length=50)
	tiempo_recorrido	= models.IntegerField()

	def __str__(self):
		return '{}'.format(self.nombre)
