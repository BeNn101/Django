# Generated by Django 5.0.2 on 2024-02-12 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Voyages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='mot_de_passe',
            new_name='password',
        ),
    ]
