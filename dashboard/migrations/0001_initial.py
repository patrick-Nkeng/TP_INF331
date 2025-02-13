# Generated by Django 5.1.4 on 2024-12-26 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomProblem', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(choices=[('Materiel', 'Materiel'), ('Logiciel', 'Logiciel')], max_length=20, null=True)),
                ('statut', models.CharField(choices=[('NON RESOLUE', 'NON RESOLUE'), ('ENCOURS', 'ENCOURS'), ('RESOLUE', 'RESOLUE')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomInterven', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.problem')),
            ],
        ),
    ]
