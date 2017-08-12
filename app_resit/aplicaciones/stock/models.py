from django.db import models
from aplicaciones.producto.models 	import Producto


class Stock(models.Model):
    disponible = models.IntegerField(default=11)
    Producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
    	return '{} '.format(self.disponible)

