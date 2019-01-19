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

    priority = lambda value : Validator.priorities[value]

    def is_number(token):
            try: int(token); return True
            except: return False

    is_operator = lambda token : token in Validator.priorities
    is_open_brace = lambda token : token == '('
    is_close_brace = lambda token : token == ')'
    is_legal = lambda  token : Validator.is_number(token) or Validator.is_operator(token)