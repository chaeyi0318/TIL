# Generated by Django 4.2.6 on 2024-11-08 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_number', models.IntegerField()),
                ('user_guess', models.IntegerField(null=True)),
                ('attempts', models.IntegerField(default=0)),
            ],
        ),
    ]
