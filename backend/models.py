import random

from django.conf import settings
from django.db import models
from django.utils import timezone


class ShortURLs(models.Model):
    origin = models.URLField(editable=False, max_length=4096)
    slug = models.SlugField(
        unique=True,
        editable=False,
        null=False,
        blank=True,
        db_index=True,
        max_length=settings.SHORT_URL_SIZE
    )
    expiration_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)

    @property
    def is_expired(self):
        return timezone.now() > self.expiration_date

    def _generate_slug(self):
        is_unique = False
        while not is_unique:
            slug_candidate = ''.join(
                random.choices(
                    settings.VALID_LETTER_POOL,
                    k=settings.SHORT_URL_SIZE
                )
            )
            if ShortURLs.objects.all().filter(slug=slug_candidate).exists():
                continue
            is_unique = True

        self.slug = slug_candidate
    
    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self._generate_slug()
        return super().save(*args, **kwargs)
