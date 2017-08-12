from django.db import models

class Logistica (models.Model):
	patente 		= models.CharField(max_length=6, primary_key=True)
	estado			= models.IntegerField(default='0',editable=False)
	vehiculo 		= models.CharField(max_length=20)
	conductor		= models.CharField(max_length=50)

