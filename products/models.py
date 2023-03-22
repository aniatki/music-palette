from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Artwork(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200)
    image_url = models.URLField()
    released = models.BooleanField()
    identifier_scheme_element = models.CharField(
        max_length=2,
        validators=[RegexValidator('^[A-Z0-9]*$',
                    'Only uppercase letters and numbers allowed.')]
        )
    issuer_code_element = models.CharField(
        max_length=5,
        validators=[RegexValidator('^[A-Z0-9]*$',
                    'Only uppercase letters and numbers allowed.')]
        )
    release_number_element = models.CharField(
        max_length=10,
        validators=[RegexValidator('^[A-Z0-9]*$',
                    'Only uppercase letters and numbers allowed.')]
        )
    check_character_element = models.CharField(
        max_length=1,
        validators=[RegexValidator('^[A-Z0-9]*$',
                    'Only uppercase letters and numbers allowed.')]
        )

    def __str__(self):
        return str(self.name)

    def GRid(self):
        """Unique Identifier for release"""
        return self.identifier_scheme_element + '-' + \
            self.issuer_code_element + '-' + \
            self.release_number_element + '-' + \
            self.check_character_element
