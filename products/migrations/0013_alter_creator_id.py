# Generated by Django 4.1.7 on 2023-03-28 18:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_artwork_price_alter_artwork_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
