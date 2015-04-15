from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    website = forms.CharField(required=False)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    

class ForgotForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
