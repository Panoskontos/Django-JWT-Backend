# Generated by Django 3.2.9 on 2022-06-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]