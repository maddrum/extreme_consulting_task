from django.views.generic import FormView

from . import forms


class CalculatorView(FormView):
    """A base view for calculations"""

    form_class = forms.CalculationForm
    template_name = 'calculator/calculator.html'
