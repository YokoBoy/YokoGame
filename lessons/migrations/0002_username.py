# Generated by Django 5.1.2 on 2024-11-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('userPassword', models.CharField(max_length=30)),
                ('userEmail', models.CharField(max_length=50)),
                ('userAbout', models.TextField(blank=True)),
                ('userTimeCreat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
