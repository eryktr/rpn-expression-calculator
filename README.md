# expression-calculator
A library that can evaluate an explicitly given expression, like `2*sin(2x*sin(x))`, using Reverse Polish Notation.

# classes
The main classes that contribute to the library are:
* `InputParser` - used to transform what the client submits into RPN
* `RPNProcessor` - used to actually evaluate the expression
* `Validator` - Helper class used in both of the above classes
* `RPNCalculator` - The facade used to encapsulate the functionality of this library. Its methods are:

# API
The below methods are the facade provided by the `RPNCalculator` class.
* `to_rpn(expression)` - Transforms the given expression to RPN. Returns a list.
* `calculate(expression, value = 0)` - Finds the mathematical value of the expression. The optional arguments is the value of any     variable found in the expression.
* `evaluate(expression, value)` = calculate(expression, value)
  
