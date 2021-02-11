from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^calculator/', include('calculator.urls', namespace='calculator')),
    url(r'^api/', include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),
]
