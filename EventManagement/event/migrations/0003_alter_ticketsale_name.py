# Generated by Django 5.0.6 on 2024-06-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_attendee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsale',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
