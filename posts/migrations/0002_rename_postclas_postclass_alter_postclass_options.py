# Generated by Django 4.0.1 on 2022-01-22 05:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostClas',
            new_name='PostClass',
        ),
        migrations.AlterModelOptions(
            name='postclass',
            options={'verbose_name': 'Posts'},
        ),
    ]
