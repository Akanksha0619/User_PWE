# Generated by Django 5.0.2 on 2024-08-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
