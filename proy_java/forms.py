# -*- coding: utf-8 -*-
import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import *


class LoginForm(AuthenticationForm):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Username")}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Password")}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                classes = self.fields[f_name].widget.attrs.get('class', '')
                classes += ' has-error'
                self.fields[f_name].widget.attrs['class'] = classes


class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Username")}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'maxlength': 60, 'class': 'form-control', 'placeholder': _("Email Address")}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Password")}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Confirm your password")}))

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class', '')
                    classes += ' has-error'
                    self.fields[f_name].widget.attrs['class'] = classes

    def clean_username(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("Account already exists."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Passwords don't match."))
        return self.cleaned_data

    
#class Compilador(forms.Form):
 #   id_codigo = id_codigo = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
    #    attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("id_codigo")}))
   # id_usuario = id_usuario = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
  #      attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("id_usuario")}))
    #link = link = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
     #   attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("link")}))
    #cod_fuente = cod_fuente = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
     #   attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("cod_fuente")}))

#    def clean (self):
 #       return self.cleaned_data
class Compilado(forms.Form):
    id_codigo = forms.CharField(label="codigo_id") 

class Compilador(forms.ModelForm):
   # id_codigo = id_codigo = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("id_codigo")}))

    class Meta:
        model = Codigo;
        
        fields =  ('id_codigo', 'id_usuario', 'link', 'cod_fuente')
       
        
            
