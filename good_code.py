import re

class Calculator:
    def __init__(self):
        self.current_value = 0


  #Static methods are used to help the main function within the program. 
  # the peek() function is used to check what the top of the stack is in order to implement postfix notation for the calculator in order to implement pemdas

    @staticmethod
    def peek(stack):
        return stack[-1] if stack else None

  # The apply operator is the one that put the whole equation together once everything is sorted, essentially, because everything will be parsed in order to implement pemdas within the calculator

    @staticmethod
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        formula = f"{left}{operator}{right}"
        values.append(eval(formula))

  # the greater_precedence() function will be the one to implement pemdas it uses a dictionary in order to implement pemdas by weighting operators in the order of pemdas.

    @staticmethod
    def greater_precedence(op1, op2):
        precedences = {'+': 0, '-': 0, '*': 1, '/': 1}
        return precedences[op1] > precedences[op2]

  # The calculate() function is the one to actually take in user input and therefore give out an output

    def calculate(self):
        user = ""
        while user != "END":
            user = input("Type in an expression (or END to quit): ")
            if user == "END":
                break

          # tokens variables uses regex to actually validate output where only the regex accepted parameters will be used in order to validate output, so the user cannot output anything crazy or output anything they wouldn't typically output in a calculator

            
            tokens = re.findall(r"\d+\.\d+|\d+|[a-zA-Z_]\w*|[+*/()-]", user)

            values, operators = [], []

          # We need to seperate values and operators in order to apply pemdas rule
          # for loop to check the accepted regex values within the string
          # the rest of the function then uses the self made functions in order to take the parsed string and pass it through parameters to enforce pemdas rules and take an input on one single line
          # it makes sure that the parsed items are going through the stack in the right order, that way pemdas is correctly enforced and the user will get the correct output.

            for token in tokens:
                
                try:
                    if '.' in token:
                        values.append(float(token))
                    else:
                        values.append(int(token))
                except ValueError:
                    
                    if token == '(':
                        operators.append(token)
                    elif token == ')':
                        while self.peek(operators) != '(':
                            self.apply_operator(operators, values)
                        operators.pop()
                    else:
                        while self.peek(operators) and self.peek(operators) not in "()":
                            if self.greater_precedence(self.peek(operators), token):
                                self.apply_operator(operators, values)
                            else:
                                break
                        operators.append(token)

            
            while self.peek(operators):
                self.apply_operator(operators, values)

            
            self.current_value = values[0]
            print("Result:", self.current_value)


# the object gets created and the function gets called.
calc = Calculator()
calc.calculate()

