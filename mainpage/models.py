from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    # __str__ - более удобное отобажение в админке
    def __str__(self):
        return self.user.name


class Event_item(models.Model):
    class Meta:
        ordering = ["-date_created"]

    #slug = models.SlugField(max_length=255, unique=True)
    #foto = models.ImageField()
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    price = models.IntegerField()

