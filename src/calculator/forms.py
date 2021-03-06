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
    number_a = forms.FloatField()
    number_b = forms.FloatField()
    operator = forms.ChoiceField(choices=OPERATOR_CHOICES)

    # validate numbers
    def clean_number_a(self):
        number_a = self.cleaned_data['number_a']
        try:
            float(number_a)
        except ValueError:
            raise forms.ValidationError(_('Invalid number A'), code=1)
        return number_a

    def clean_number_b(self):
        number_b = self.cleaned_data['number_b']
        try:
            float(number_b)
        except ValueError:
            raise forms.ValidationError(_('Invalid number B'), code=2)
        return number_b

    def clean(self):
        cleaned_data = super().clean()
        number_b = cleaned_data.get('number_b', None)
        if number_b is None:
            return
        operator = cleaned_data.get('operator')
        if operator == '/' and number_b == 0:
            raise forms.ValidationError('Division by zero', code=3)
