from django.db import models
from random import choices
from string import ascii_letters, digits

# Create your models here.
class LinkMap(models.Model):
    redirects_to = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    times_followed = models.PositiveIntegerField(default=0)

    def random_string(self, n):
        return ''.join(
            choices(ascii_letters + digits, k=n)
        )

    def generate_short_url(self):
        url = self.random_string(10)

        while LinkMap.objects.filter(short_url=url).exists():
            url = self.random_string(10)

        return url
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()

        super().save(*args, **kwargs)
