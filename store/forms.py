# -*- coding: utf-8 -*-
from django.forms import ModelForm 
from django import forms 
from django.contrib.auth.models import User
from store.models import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
            'email':forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'maxlength':255}),

        }

        error_messages={
            'username':{
                'required':'Campo obrigatório'
            },
            'email':{
                'required':'Campo obrigatório'
            },
            'password':{
                'required':'Campo obrigatório'
            },
        }
    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user  