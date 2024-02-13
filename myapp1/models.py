from django.db import models

class Etudiant(models.Model):
    name = models.CharField(max_length=250)
    prenom = models.TextField()
    tel=models.TextField()
    def __str__(self):
        return self.name
