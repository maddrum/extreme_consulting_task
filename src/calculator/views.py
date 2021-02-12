from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from calculator import forms
from common_modules.calculator_module import Calculator


class CalculatorView(FormView):
    """A base view for calculations"""

    form_class = forms.CalculationForm
    template_name = 'calculator/calculator.html'
    result = None

    def form_valid(self, form):
        """If no result - returns form_invalid"""
        calculator = Calculator(number_a=form.cleaned_data['number_a'],
                                number_b=form.cleaned_data['number_b'],
                                operator=form.cleaned_data['operator'])
        self.result = calculator.calculate_result()
        if self.result is None:
            form.add_error(None, _('General input data error'))
            return super().form_invalid(form)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        success_url = reverse_lazy('calculator:calculator_view')
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = self.result
        return context
