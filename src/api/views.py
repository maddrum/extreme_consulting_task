from rest_framework import viewsets
from api.serializers import InputSerializer


class RestCalculatorView(viewsets.ViewSet):
    http_method_names = ['get', 'post']
