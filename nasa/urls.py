from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework import routers
from nasa.views import PictureViewSet


router = routers.DefaultRouter()
router.register(r'picture', PictureViewSet, 'Picture')

urlpatterns = [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^admin/', admin.site.urls, name='admin'),
        url(r'^', include(router.urls, namespace='api')),
        ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
