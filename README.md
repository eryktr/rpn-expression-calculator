# expression-calculator
A library that can evaluate an explicitly given expression, like `2sin(2xsin(x))`, using Reverse Polish Notation.

# Classes
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

# Usage
The API can be used to calculate both raw and parametrized expressions.

## Rules:
 * Functions can be nested, but every parameter needs to be properly parenthesized. `sin(sin(sin(sin(pi/2))))`
 * There are two built-in constants: `pi` and `e`.
 * When there is no operator, multiplication is implied. `pie = 8.53973422267`
 * The asterisk should be used when multiplying an expression in parentheses by a number IF the number appears after the parentheses. For example, `2(2+2)` is fine, but `(2+x)2` is not a standard way to write such expressions, and so is not allowed. Yet, `(2+x)(2+x)` is perfectly fine.
 
## Supported operators:
* `*` - multiplication
* `/` - division
* `+` - addition
* `-` - subtraction
* `^` - exponentation

## Supported functions:
* `sin()`
* `cos()`
* `tan()`
* `cot()`
* `log()` - natural logarithm
* `asin()` - inverse sine
* `acos()`
* `atan()`
* `sinh()` - hyperbolic sine
* `cosh()`
* `tanh()`
* `abs()` - absolute value
