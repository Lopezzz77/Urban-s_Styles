from django.db import models

# clss+name 

class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    Nombre_producto = models.TextField(max_length=60, unique=True)
    stock = models.IntegerField()
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField()
    


    def __str__(self):
        return self.id
