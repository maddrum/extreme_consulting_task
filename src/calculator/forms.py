from django import forms
from django.utils.translation import ugettext_lazy as _


class CalculationForm(forms.Form):
    """Base calculation form."""

    OPERATOR_CHOICES = (
        ('+', _('Addition')),
        ("-", _('Subtraction')),
        ("*", _('Multiplication')),
        ("/", _('Division')),

    )
    number_A = forms.FloatField()
    number_B = forms.FloatField()
    operator = forms.ChoiceField(choices=OPERATOR_CHOICES)

