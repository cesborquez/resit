from django.db import models

from aplicaciones.producto.models   import Producto
from aplicaciones.logistica.models 	import Logistica
from aplicaciones.cliente.models 	import Cliente


class Pedido (models.Model):
	codigo		 	= models.AutoField(primary_key=True)
	fecha_pedido 	= models.DateTimeField(auto_now=True)
	fecha_confir	= models.DateTimeField(null=True,editable=False)
	fecha_entrega	= models.DateTimeField(null=True,editable=False)
	estado			= models.IntegerField(default='0',editable=False)
	cantidad 		= models.IntegerField(blank=True,)
	Producto 		= models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	Logistica 		= models.ForeignKey(Logistica, null=True, blank=True, on_delete=models.CASCADE)
	Cliente    	    = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)

	