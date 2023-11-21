from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'lot', 'quantity', 'category', 'expiration_date', 'observation')
        labels = {
            'name': 'Nome',
            'lot': 'Lote',
            'quantity': 'Quantidade',
            'category': 'Categoria',
            'expiration_date': 'Validade',
            'observation': 'Observação',
        }
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'observation': forms.Textarea(attrs={'rows': 6, 'cols': 15}),
        }