from dataclasses import field
from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label = "password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password'
            }
        )
    )

    password2 = forms.CharField(
        label = "re-password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'repeat password'
            }
        )
    )

    class Meta:
        model= User
        fields = (
            'UserName',
            'Email',
            'Name',
            'LastName',
            'CompanyName',
        )

    def clean_password2(self):
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            self.add_error("password2", "Passwords are not the same")

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "username",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'class': 'form-control form-control-lg',
            }
        )
    )

    password = forms.CharField(
        label = "password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class': 'form-control form-control-lg',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if not authenticate(username = username, password = password):
            #self.add_error("username", "Wrong credentials")
            raise forms.ValidationError('Wrong credentials')
            

        return self.cleaned_data