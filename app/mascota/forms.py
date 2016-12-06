from django import forms
from app.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota #aqui se indica con q modelo se va a trabajar el formulario
        #campos que saldran en el FORM tomando de ejemplo los que estan en la BDD
        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        #aqui se declaran como se veran los LABEL de cada campo en la tupla
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad Aproximada',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }
        #Estos widgets son los que se van a pintar como etiquetas HTML, ponerlo como un textbox, select(este es una llave foranea manytomany),checkbox, entre otros.
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }