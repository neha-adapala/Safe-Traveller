from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreateInForum(ModelForm):
	class Meta:
		model = forum
		fields = "__all__"


class CreateInDiscussion(ModelForm):
	class Meta:
		model = Discussion
		fields = "__all__"

from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))