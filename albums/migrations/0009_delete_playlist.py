# Generated by Django 4.1.2 on 2022-10-24 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_remove_album_album_cover_album_song_album_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Playlist',
        ),
    ]
