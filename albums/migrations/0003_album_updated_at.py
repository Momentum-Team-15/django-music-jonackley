# Generated by Django 4.1.2 on 2022-10-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]