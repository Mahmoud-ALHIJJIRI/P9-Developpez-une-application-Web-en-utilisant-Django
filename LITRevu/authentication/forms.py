from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import MinLengthValidator


class UserForm(forms.Form):
    first_name = forms.fields.CharField(max_length=30)
    last_name = forms.fields.CharField(max_length=30)
    age = forms.fields.IntegerField()
    email_address = forms.fields.CharField(max_length=30)
    password = forms.fields.CharField(max_length=32)
    password1 = forms.fields.CharField(max_length=32)

# forms.py
class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
