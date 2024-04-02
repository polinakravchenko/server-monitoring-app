from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)