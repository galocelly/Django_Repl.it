#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from myapp.models import *

class UserRegForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.CharField(widget=forms.EmailInput,label='Correo')
    password1 = forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Ingresa tu password de nuevo')

    class Meta:
        model = User
        fields = ('username','email')

    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})

class CodeForm(forms.ModelForm):

    code = forms.CharField(widget=forms.Textarea(attrs={'rows': 40, 'cols': 100}),label='')
    nombre_codigo = forms.CharField(label='')

    class Meta:
        model = Codigos
        fields = ('nombre_codigo','code')
        exclude = ['user']

    def __init__(self, *args, **kwargs):

        super(CodeForm, self).__init__(*args, **kwargs)
        self.fields['nombre_codigo'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Nombre del Archivo'})
        self.fields['code'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Escribe tu Codigo aqui'})
