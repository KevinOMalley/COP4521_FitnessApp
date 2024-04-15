from django import forms
from django.contrib.auth.forms import UserCreationForm
from HealthTracker.models import Account

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')