# Generated by Django 4.1.3 on 2023-07-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email address'),
        ),
    ]