import datetime

from django.utils import timezone
from rest_framework import serializers

from .models import ShortURLs


class ShortURLsSerializer(serializers.ModelSerializer):
    origin = serializers.URLField()
    days_to_expire = serializers.IntegerField(
        min_value=1,
        write_only=True
    )

    class Meta:
        model = ShortURLs
        fields = ('origin', 'slug', 'expiration_date', 'creation_date', 'days_to_expire', 'is_expired')
        read_only_fields = ('slug', 'expiration_date', 'creation_date', 'is_expired')


    def validate(self, attrs):
        days_to_expire = attrs.pop('days_to_expire')
        attrs['expiration_date'] = timezone.now() + datetime.timedelta(days=days_to_expire)
        return super().validate(attrs)

