from django.test import TestCase
from calculator.forms import CalculationForm


# Test form
class TestInputForm(TestCase):
    valid_operators = ['+', '-', '*', '/']
    non_valid_operators = [1, -5, 'a', '~', '^', '&', '%']

    def test_valid_form_plus(self):
        for operator in self.valid_operators:
            form_data = {
                'number_a': 5,
                'number_b': -3,
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertTrue(form.is_valid(), msg='[ERROR] valid data')

    def test_form_wrong_number_a(self):
        for operator in self.valid_operators:
            form_data = {
                'number_a': 'a',
                'number_b': 5,
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertFalse(form.is_valid(), msg='[ERROR] number_a validation')

    def test_form_wrong_number_b(self):
        for operator in self.valid_operators:
            form_data = {
                'number_a': 5,
                'number_b': 'b',
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertFalse(form.is_valid(), msg='[ERROR] number_b validation')

    def test_form_wrong_operator(self):
        for operator in self.non_valid_operators:
            form_data = {
                'number_a': 5,
                'number_b': 2,
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertFalse(form.is_valid(), msg='[ERROR] Not supported operator validation')

    def test_form_zero_division(self):
        form_data = {
            'number_a': 5,
            'number_b': 0,
            'operator': '/'
        }
        form = CalculationForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='[ERROR] zero division validation')
