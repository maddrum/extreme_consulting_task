from django.conf.urls import url

app_name = 'calculator'
from . import views

urlpatterns = [
    url(r'^$', views.CalculatorView.as_view(), name='calculator_view'),
]
