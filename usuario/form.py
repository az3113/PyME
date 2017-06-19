
from django import forms
from .models import User , UserProfile , ProfileImage , Category

class FormularioUsuario(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email","password"]
		widgets = {
			"password":forms.TextInput(attrs={"type":"password"})

		}



class FormularioPerfil(forms.ModelForm):
	categoria = forms.ModelChoiceField(queryset=Category.objects.all(),initial=0)
	class Meta:
		model = UserProfile
		fields = ["companyname","companyconcept","contact","companyservice"]


class FormularioImagen(forms.ModelForm):
	class Meta:
		model = ProfileImage
		fields = ["companyimage","biography"]
		widgets = {
				'companyimage' : forms.FileInput(attrs = {'accept': 'image/gif, image/jpeg, image/png'}),
				'biography' : forms.FileInput(attrs = {'accept': 'image/gif, image/jpeg, image/png'}),
		}

		