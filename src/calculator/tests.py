from django.test import TestCase
from calculator.forms import CalculationForm
from django.test import Client
from django.urls import reverse_lazy
import random

client = Client()
valid_operators = ['+', '-', '*', '/']
non_valid_operators = [1, -5, 'a', '~', '^', '&', '%']


# Test form
class TestInputForm(TestCase):

    def test_valid_form_plus(self):
        for operator in valid_operators:
            form_data = {
                'number_a': 5,
                'number_b': -3,
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertTrue(form.is_valid(), msg='[ERROR] valid data')

    def test_form_wrong_number_a(self):
        for operator in valid_operators:
            form_data = {
                'number_a': 'a',
                'number_b': 5,
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertFalse(form.is_valid(), msg='[ERROR] number_a validation')

    def test_form_wrong_number_b(self):
        for operator in valid_operators:
            form_data = {
                'number_a': 5,
                'number_b': 'b',
                'operator': operator
            }
            form = CalculationForm(data=form_data)
            self.assertFalse(form.is_valid(), msg='[ERROR] number_b validation')

    def test_form_wrong_operator(self):
        for operator in non_valid_operators:
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


# View test
class TestCalculatorView(TestCase):
    def test_math_output(self):
        form_data = []
        # generate random math form data
        for item in range(50):
            # generate random float numbers
            divider = random.randint(-100000, 100000)
            if divider == 0:
                divider = 0.1
            number_a = random.randint(-100000, 100000) / divider
            number_b = random.randint(-100000, 100000) / divider
            # not null number_b (zero division)
            if number_b == 0:
                number_b = 0.1
            # handle addition
            temp_dict_plus = {
                'number_a': number_a,
                'number_b': number_b,
                'operator': '+',
                'result': number_a + number_b,
            }
            form_data.append(temp_dict_plus)
            # handle subtraction
            temp_dict_minus = {
                'number_a': number_a,
                'number_b': number_b,
                'operator': '-',
                'result': number_a - number_b,
            }
            form_data.append(temp_dict_minus)
            # handle multiplication
            temp_dict_multiplication = {
                'number_a': number_a,
                'number_b': number_b,
                'operator': '*',
                'result': number_a * number_b,
            }
            form_data.append(temp_dict_multiplication)
            # handle division
            temp_dict_division = {
                'number_a': number_a,
                'number_b': number_b,
                'operator': '/',
                'result': number_a / number_b,
            }
            form_data.append(temp_dict_division)
        # process generated data
        for input_data in form_data:
            response = client.post(reverse_lazy('calculator:calculator_view'), data=input_data)
            result = response.context_data.get('result')
            if result != input_data['result']:
                print('-' * 10)
                test_case = f'Tested {input_data["number_a"]} {input_data["operator"]} {input_data["number_b"]}'
                print(test_case)
                print(f'Should have returned: {input_data["result"]}')
                print(f'It returned: {result}')
                print('-' * 10)
                raise AssertionError
