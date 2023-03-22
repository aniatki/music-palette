# Generated by Django 4.1.7 on 2023-03-22 22:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('released', models.BooleanField()),
                ('identifier_scheme_element', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^[A-Z0-9]*$', 'Only uppercase letters and underscores allowed.')])),
                ('issuer_code_element', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[A-Z0-9]*$', 'Only uppercase letters and underscores allowed.')])),
                ('release_number_element', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[A-Z0-9]*$', 'Only uppercase letters and underscores allowed.')])),
                ('check_character_element', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[A-Z0-9]*$', 'Only uppercase letters and underscores allowed.')])),
            ],
        ),
    ]
