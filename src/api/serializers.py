from rest_framework import serializers

from calculator.forms import CalculationForm


class InputSerializer(serializers.Serializer):
    number_a = serializers.FloatField()
    number_b = serializers.FloatField()
    operator = serializers.ChoiceField(choices=CalculationForm().OPERATOR_CHOICES)

    def validate(self, data):
        if data['operator'] == '/' and data['number_b'] == 0:
            raise serializers.ValidationError("Division by zero")
        return data


class ResultSerializer(serializers.Serializer):
    result = serializers.FloatField()
