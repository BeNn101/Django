from django import forms

class ConnexionForm(forms.Form):
    email = forms.EmailField(label='Adresse e-mail')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
