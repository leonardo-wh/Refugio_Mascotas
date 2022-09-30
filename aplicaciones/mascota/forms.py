from django import forms

from aplicaciones.mascota.models import Mascota
from image_uploader_widget.widgets import ImageUploaderWidget

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
			'imagen',

		]

		labels = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad aproximada',
			'fecha_rescate': 'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
			
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),

		}