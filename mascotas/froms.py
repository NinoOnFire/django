from django import forms
from .models import Cliente, Solicitud

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Run_Cliente', 'Nombre_Cliente', 'Apellido', 'Correo', 'Telefono']
        widgets = {
            'Run_Cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese RUN del cliente'}),
            'Nombre_Cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese apellido'}),
            'Correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono'}),
        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['Nombre_Mascota', 'Detalle']
        widgets = {
            'Nombre_Mascota': forms.Select(attrs={'class': 'form-select'}),
            'Detalle': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ingrese el detalle de la solicitud'}),
        }