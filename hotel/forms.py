from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from hotel.models import Receptionist

class UserRegisterForm(UserCreationForm):
    emails = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReceptionistRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    class Meta:
        model = Receptionist
        fields = ['first_name', 'last_name', 'gender']