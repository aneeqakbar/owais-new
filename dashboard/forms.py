from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client

class ClientCreateForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name']

class ClientUpdateForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name']
