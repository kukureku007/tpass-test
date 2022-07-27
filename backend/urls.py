from django.urls import include, path
from rest_framework import routers

from . import views


app_name = 'urls-backend'
router = routers.DefaultRouter()

router.register(
    r'urls',
    views.ShortURLsViewSet,
    basename='urls'
)


urlpatterns = [
    path('', include(router.urls)),
    path('<slug:slug>', views.redirect_short_url)
]