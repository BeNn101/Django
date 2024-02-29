from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home (request):
    return render (request, 'home.html', {})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            utilisateur = authenticate(request, username=username, password=password)
            
            print(utilisateur)  
            if utilisateur is not None:
                login(request, utilisateur)
                return redirect('Voyages:home')  
            else:
                
                form.add_error(None, "Identifiants incorrects. Veuillez réessayer.")
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate ( username=username, password=password )
            login(request,user)
            messages.success (request , ("Vous avez bien été enregistrer")) 
            
            return redirect ('')
    else : 
        form = UserCreationForm()
    return render(request, 'register_user.html' , {'form':form})
