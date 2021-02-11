from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializers


class RestCalculatorView(APIView):
    serializer_class = serializers.InputSerializer

    def get(self, request):
        return Response('input number_a, number_b and operator')

    def post(self, request, *args, **kwargs):
        return Response('The result is: ')
