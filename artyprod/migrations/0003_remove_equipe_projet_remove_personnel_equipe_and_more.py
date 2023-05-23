# Generated by Django 4.2.1 on 2023-05-06 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0002_remove_equipe_personnels_remove_projet_equipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='projet',
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='equipe',
        ),
        migrations.AddField(
            model_name='equipe',
            name='personnels',
            field=models.ManyToManyField(to='artyprod.personnel'),
        ),
        migrations.AddField(
            model_name='projet',
            name='equipe',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='artyprod.equipe'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('dg', 'Design Graphique'), ('pa', 'Production Audiovisuelle'), ('c3d', 'Conception 3D')], default='dg', max_length=255),
        ),
    ]
