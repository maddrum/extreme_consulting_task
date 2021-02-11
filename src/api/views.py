from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.views import APIView

from api import serializers
from calculator.views import CalculatorView


class RestCalculatorView(APIView):
    serializer_class = serializers.InputSerializer

    def get(self, request):
        return Response('Input number_a, number_b and operator')

    def post(self, request, *args, **kwargs):
        serializer = serializers.InputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)
        result_serializer = serializers.ResultSerializer()
        data = result_serializer.data
        number_a = float(request.data.get('number_a'))
        number_b = float(request.data.get('number_b'))
        operator = request.data.get('operator')
        calculation_result = CalculatorView().calculate_result(a=number_a, b=number_b, operator=operator)
        # handle ok result
        data['result'] = calculation_result
        return Response(data, status=HTTP_200_OK)
