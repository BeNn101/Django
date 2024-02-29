from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
