# Generated by Django 4.1.7 on 2023-03-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_artwork_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='image_url',
        ),
        migrations.AddField(
            model_name='artwork',
            name='image',
            field=models.ImageField(blank=True, upload_to='artworks/'),
        ),
    ]
