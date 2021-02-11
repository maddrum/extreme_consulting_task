from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from api import views

app_name = 'api'
router = DefaultRouter()
router.register('calculator', views.RestCalculatorView, basename='rest_calculator')

# rest framework schema
rest_schema_view = get_schema_view(title='Calculator API')

urlpatterns = [
    url(r'', include(router.urls)),
]
