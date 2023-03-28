from django.db import models

# Create your models here.


class Creator(models.Model):
    """
    Model for user object
    """
    ACCOUNT_TYPE_CHOICES = [
        ("0", "Art Creator"),
        ("1", "Record Label or Musician"),
    ]

    name = models.CharField(
        max_length=75,
        blank=False,
        null=False)
    username = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False)
    email = models.EmailField(
        max_length=75,
        unique=True,
        blank=False,
        null=False)
    account_type = models.CharField(max_length=24, choices=ACCOUNT_TYPE_CHOICES)

    def __str__(self):
        return str(self.name)


class Artwork(models.Model):
    """
    Model for Artwork that will be published from creators
    """

    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='artworks/', blank=True)
    released = models.BooleanField()
    isrc = models.CharField(max_length=12, blank=True)
    date_posted = models.DateField(auto_now_add=True, null=True)
    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
