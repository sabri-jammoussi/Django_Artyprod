# Generated by Django 4.2.1 on 2023-05-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0003_remove_equipe_projet_remove_personnel_equipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
