class Validator:

    priorities = {
        '+' : 1,
        '-' : 1,
         '*' : 2,
        '/' : 2,
        '%' : 2,
        '^' : 3,
        '(' : -100,
        ')' : -100
    }
    priority = lambda value : Validator.priorities.get(value, 100)
    is_operator = lambda token : token in Validator.priorities
    is_open_brace = lambda token : token == '('
    is_close_brace = lambda token : token == ')'
    
    variables = {'x'}
    is_variable = lambda token : token in Validator.variables

    functions = {'sin', 'cos', 'tan', 'cot', 'log'}
    is_function = lambda token : token in Validator.functions

    constants = {"pi", "e"}
    is_const = lambda token : token in Validator.constants

    is_numeric = lambda token : Validator.is_number(token) or Validator.is_const(token) \
                                or Validator.is_variable(token)

    def is_number(token):
            try: int(token); return True
            except: return False
 
    is_legal = lambda  token : Validator.is_numeric(token) or Validator.is_operator(token) \
                                or Validator.is_function(token)
    is_illegal = lambda token : not(Validator.is_legal(token))
    