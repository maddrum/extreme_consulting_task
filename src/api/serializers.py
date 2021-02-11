from rest_framework import serializers
from calculator.forms import CalculationForm


class InputSerializer(serializers.Serializer):
    number_a = serializers.FloatField()
    number_b = serializers.FloatField()
    operator = serializers.ChoiceField(choices=CalculationForm().OPERATOR_CHOICES)
