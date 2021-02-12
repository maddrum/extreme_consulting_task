class Calculator:
    """
    Perform calculation action based on number input and given operator
    """
    result = None

    def __init__(self, number_a, number_b, operator):
        """
        :param number_a: - [float] - number a
        :param number_b: - [float] - number a
        :param operator: - [+,-,*,/] - math operator
        """

        self.number_a = number_a
        self.number_b = number_b
        self.operator = operator

    def calculate_result(self):
        """
        :return: result of the math operation or None on wrong data
        """
        result = None
        if self.operator == '+':
            result = self.number_a + self.number_b
        elif self.operator == '-':
            result = self.number_a - self.number_b
        elif self.operator == '*':
            result = self.number_a * self.number_b
        elif self.operator == '/':
            result = self.number_a / self.number_b
        return result
