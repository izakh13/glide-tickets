# Generated by Django 5.1.7 on 2025-03-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('choose_value', '--Choose a right value--'), ('adult', 'Adult'), ('children', 'Children')], default='choose_value', max_length=100)),
                ('means_of_transport', models.CharField(choices=[('choose_value', '--Choose a right value--'), ('airplane', 'Airplane'), ('coach', 'Coach'), ('train', 'Train')], default='choose_value', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('where_from', models.CharField(max_length=100)),
                ('where_to', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
    ]
