from django import forms

class UserSimpleForm(forms.Form):
    nro_data = forms.IntegerField(
        label="Cantidad de Datos:", 
        max_value=1000, 
        min_value=1, 
        required=True
    )
    dominio = forms.CharField(
        label="Dominio:", 
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'example.com'
        })
    )