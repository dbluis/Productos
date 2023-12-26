from django.db import models

class MaterialGramos(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_comprada_gramos = models.IntegerField(blank=True, null=True)
    costo_gramos = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class MaterialUnitario(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_comprada_unidades = models.IntegerField(blank=True, null=True)
    costo_unidades = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class RelacionProductoMaterial(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    material_unitario = models.ForeignKey(MaterialUnitario, on_delete=models.CASCADE, null=True, blank=True)
    material_gramos = models.ForeignKey(MaterialGramos, on_delete=models.CASCADE, null=True, blank=True)
    # No me sirve la cantidad comprada aqui
    cantidad_comprada = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    # Esto si
    cantidad_utilizada = models.DecimalField(max_digits=10, decimal_places=2)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    relacion_materiales_gramos = models.ManyToManyField(MaterialGramos, through=RelacionProductoMaterial, related_name='materiales_gramos')
    relacion_materiales_unitarios = models.ManyToManyField(MaterialUnitario, through=RelacionProductoMaterial, related_name='materiales_unitarios')

    # Esto tampo me sirve aqui
    cantidad_utilizada = models.IntegerField(null=True, blank=True)

    def costo_total(self):
        costo_total_unitario = 0
        costo_total_gramos = 0

        for relacion in self.relacionproductomaterial_set.all():
            if relacion.material_unitario and relacion.material_unitario.costo_unidades is not None and relacion.cantidad_utilizada is not None:
                costo_total_unitario += (relacion.cantidad_utilizada / relacion.cantidad_comprada) * relacion.material_unitario.costo_unidades

            if relacion.material_gramos and relacion.material_gramos.costo_gramos is not None and relacion.cantidad_utilizada is not None:
                costo_total_gramos += (relacion.cantidad_utilizada / relacion.cantidad_comprada) * relacion.material_gramos.costo_gramos

        return costo_total_unitario + costo_total_gramos

    def __str__(self):
        return self.nombre
