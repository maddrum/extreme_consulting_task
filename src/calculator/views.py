from django.urls import reverse_lazy
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _
from . import forms


class CalculatorView(FormView):
    """A base view for calculations"""

    form_class = forms.CalculationForm
    template_name = 'calculator/calculator.html'
    result = None

    @staticmethod
    def calculate_result(a, b, operator):
        result = None
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        return result

    def form_valid(self, form):
        self.result = self.calculate_result(a=form.cleaned_data['number_a'],
                                            b=form.cleaned_data['number_b'],
                                            operator=form.cleaned_data['operator'])
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
