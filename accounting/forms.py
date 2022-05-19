from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(forms.ModelForm):
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm-password does not match"
            )
        return password2


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
