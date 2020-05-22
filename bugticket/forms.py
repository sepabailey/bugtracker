from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'password1', 'password2')


class TicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
