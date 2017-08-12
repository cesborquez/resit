from django.db import models



class Producto (models.Model):
	id_prod 	= models.AutoField(primary_key=True)
	nombre		= models.CharField(max_length=50)

	def __str__(self):
		return '{} '.format( self.nombre)


