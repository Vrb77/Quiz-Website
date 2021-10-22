from django import forms  
from quiz_app.models import *#queModel
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class c1Form(forms.ModelForm):
	class Meta:
		model=c1Model
		fields="__all__"
class c2Form(forms.ModelForm):
	class Meta:
		model=c2Model
		fields="__all__"

class p1Form(forms.ModelForm):
	class Meta:
		model=p1Model
		fields="__all__"
class p2Form(forms.ModelForm):
	class Meta:
		model=p2Model
		fields="__all__"

class m1Form(forms.ModelForm):
	class Meta:
		model=m1Model
		fields="__all__"
class m2Form(forms.ModelForm):
	class Meta:
		model=m2Model
		fields="__all__"

class b1Form(forms.ModelForm):
	class Meta:
		model=b1Model
		fields="__all__"
class b2Form(forms.ModelForm):
	class Meta:
		model=b2Model
		fields="__all__"

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class contactForm(forms.ModelForm):
	class Meta:
		model=contact
		fields="__all__"






