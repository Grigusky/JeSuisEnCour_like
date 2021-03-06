# Generated by Django 2.0.1 on 2018-01-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absences_Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Absences_Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('justificatif', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('intitule', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Eleves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prof_Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Prof')),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=50)),
                ('annee', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Promotions')),
            ],
        ),
        migrations.CreateModel(
            name='Specialite_Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Eleves')),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Specialite')),
            ],
        ),
        migrations.AddField(
            model_name='prof_promotion',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Promotions'),
        ),
        migrations.AddField(
            model_name='cours',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Promotions'),
        ),
        migrations.AddField(
            model_name='absences_prof',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Cours'),
        ),
        migrations.AddField(
            model_name='absences_prof',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Prof'),
        ),
        migrations.AddField(
            model_name='absences_eleve',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Cours'),
        ),
        migrations.AddField(
            model_name='absences_eleve',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Eleves'),
        ),
    ]
