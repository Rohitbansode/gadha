# Generated by Django 5.0.4 on 2024-05-12 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='title_text',
            new_name='title',
        ),
    ]
