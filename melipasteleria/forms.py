# productos/forms.py
from django import forms
from .models import MaterialGramos, MaterialUnitario, RelacionProductoMaterial, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad_utilizada', 'relacion_materiales_gramos', 'relacion_materiales_unitarios']
        widgets = {
            'relacion_materiales_gramos': forms.CheckboxSelectMultiple,
            'relacion_materiales_unitarios':forms.CheckboxSelectMultiple
        }


class RelacionProductoMaterialGramosForm(forms.ModelForm):
    class Meta:
        model = RelacionProductoMaterial
        fields = ['material_gramos', 'cantidad_utilizada']

class RelacionProductoMaterialUnitarioForm(forms.ModelForm):
    class Meta:
        model = RelacionProductoMaterial
        fields = ['material_unitario', 'cantidad_utilizada']

class Material_unitario(forms.ModelForm):
    class Meta:
        model = MaterialUnitario
        fields = ['nombre', 'cantidad_comprada_unidades', 'costo_unidades']

class Material_gramos(forms.ModelForm):
    class Meta:
        model = MaterialGramos
        fields = ['nombre', 'cantidad_comprada_gramos', 'costo_gramos']