from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from rest_framework import mixins, viewsets

from .serializers import ShortURLsSerializer
from .models import ShortURLs


def redirect_short_url(request, slug):
    short: ShortURLs = get_object_or_404(ShortURLs, slug=slug)

    if short.is_expired:
        return HttpResponseNotFound(f'This link \'{slug}\' is expired.')
    return redirect(to=short.origin)

class ShortURLsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = ShortURLs.objects.all()
    serializer_class = ShortURLsSerializer