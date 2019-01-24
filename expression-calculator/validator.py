class Validator:
    priorities = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3,
        '(': -100,
        ')': -100
    }

    @staticmethod
    def priority(value):
        return Validator.priorities.get(value, 100)

    @staticmethod
    def is_operator(token):
        return token in Validator.priorities

    @staticmethod
    def is_open_brace(token):
        return token == '('

    @staticmethod
    def is_close_brace(token):
        return token == ')'

    variables = {'x'}

    @staticmethod
    def is_variable(token):
        return token in Validator.variables

    functions = {'sin', 'cos', 'tan', 'cot', 'log', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh', 'abs'}

    @staticmethod
    def is_function(token):
        return token in Validator.functions

    constants = {"pi", "e"}

    @staticmethod
    def is_const(token):
        return token in Validator.constants

    @staticmethod
    def is_numeric(token):
        return Validator.is_number(token) \
               or Validator.is_const(token) \
               or Validator.is_variable(token)

    @staticmethod
    def is_number(token):
        try:
            int(token); return True
        except:
            return False

    @staticmethod
    def is_legal(token):
        return Validator.is_numeric(token) \
            or Validator.is_operator(token) \
            or Validator.is_function(token)

    @staticmethod
    def is_illegal(token):
        return not (Validator.is_legal(token))
