from django.contrib import admin
from .models import MaterialGramos, MaterialUnitario, RelacionProductoMaterial, Producto
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ['relacion_materiales_gramos', 'relacion_materiales_unitarios']


admin.site.register(Producto)
admin.site.register(MaterialGramos)
admin.site.register(MaterialUnitario)
admin.site.register(RelacionProductoMaterial)