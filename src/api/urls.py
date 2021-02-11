from django.conf.urls import url

from api import views

app_name = 'api'

urlpatterns = [
    url(r'^calculator/$', views.RestCalculatorView.as_view()),
]
