from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^rest/', include('rest.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
