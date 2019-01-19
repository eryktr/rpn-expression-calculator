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

    functions_num_params_map = {
            'sin' : 1,
            'cos' : 1,
            'tan' : 1,
            'cot' : 1,
    }

    num_args = lambda token : Validator.functions_num_params_map[token]

    priority = lambda value : Validator.priorities[value]

    def is_number(token):
            try: int(token); return True
            except: return False
 
    is_operator = lambda token : token in Validator.priorities
    is_function = lambda token : token in Validator.functions_num_params_map
    is_open_brace = lambda token : token == '('
    is_close_brace = lambda token : token == ')'
    is_legal = lambda  token : Validator.is_number(token) or Validator.is_operator(token) or Validator.is_function(token)
    