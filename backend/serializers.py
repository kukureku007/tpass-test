import datetime

from django.utils import timezone
from rest_framework import serializers

from .models import ShortURLs


class ShortURLsSerializer(serializers.ModelSerializer):
    origin = serializers.CharField()
    days_to_expire = serializers.IntegerField(min_value=1, write_only=True)

    class Meta:
        model = ShortURLs
        fields = ('origin', 'slug', 'expiration_date', 'creation_date', 'days_to_expire', 'is_expired')
        read_only_fields = ('slug', 'expiration_date', 'creation_date', 'is_expired')

    def create(self, validated_data):
        days_to_expire = validated_data.pop('days_to_expire')

        validated_data['expiration_date'] = timezone.now() + datetime.timedelta(days=days_to_expire)
        return super().create(validated_data)
