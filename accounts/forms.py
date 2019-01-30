from .models import User, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm as UserForm


class UserCreationForm(UserForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'full_name', 'fingercode']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'group', 'image', 'bio']


class ChangePassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_pass1 = forms.CharField(widget=forms.PasswordInput)
    new_pass2 = forms.CharField(widget=forms.PasswordInput)
