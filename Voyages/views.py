from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            utilisateur = authenticate(request, email=email, password=password)
            if utilisateur is not None:
                login(request, utilisateur)
                return redirect('accueil')  
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', {'form': form})
