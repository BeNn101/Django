from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Voyage(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    date_depart = models.DateField()
    date_retour = models.DateField()

    def __str__(self):
        return f"{self.utilisateur.nom} - {self.destination}"

class Vol(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    compagnie = models.CharField(max_length=100)
    numero_vol = models.CharField(max_length=20)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()

    def __str__(self):
        return f"{self.compagnie} - {self.numero_vol}"

class Hebergement(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.nom
