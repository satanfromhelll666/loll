from __future__ import division
import random

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}

### INFIX ===> POSTFIX ###
'''
1)Fix a priority level for each operator. For example, from high to low:
    3.    - (unary negation)
    2.    * /
    1.    + - (subtraction)
2) If the token is an operand, do not stack it. Pass it to the output. 
3) If token is an operator or parenthesis:
    3.1) if it is '(', push
    3.2) if it is ')', pop until '('
    3.3) push the incoming operator if its priority > top operator; otherwise pop.
    *The popped stack elements will be written to output. 
4) Pop the remainder of the stack and write to the output (except left parenthesis)
'''


def infix_to_postfix(formula):
    stack = []  # only pop when the coming op has priority
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack:
        output += stack.pop()
    # print (output)
    return output


### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op+b+a)
            op_stack.pop()  # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op+b+a)
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op+b+a)
    # print (exp_stack[-1])
    return exp_stack[-1]


def _print(output, sourceOfInput, path):
    if(sourceOfInput is "console"):
        print(output)
    else:
        file = open(path, 'a+')
        file.write(f"\n{output}")
        file.close()
        


def operationOnIput(expression, sourceOfInput, path):
    while(True):
        print("Covert To: ")
        print("1. Prefix")
        print("2. Postfix")
        print("3. Go back")
        response = int(input("choice: "))
        if(response == 1):
            output = infix_to_prefix(expression)
            _print(output, sourceOfInput, path)
        elif(response == 2):
            output = infix_to_postfix(expression)
            _print(output, sourceOfInput, path)
        elif(response == 3):
            break
        else:
            print("Choose from the given options!")


def main():
    while(True):
        print("Choose an option: ")
        print("1. Console Input")
        print("2. File Input")
        print("3. Exit")
        response = int(input("choice: "))
        if(response == 1):
            # input from console
            sourceOfInput = "console"
            expression = input("Type an infix expression: ")
            operationOnIput(expression, sourceOfInput, None)
        elif(response == 2):
            sourceOfInput = "file"
            path = r""+input("Type the address of the file: ")
            file = open(path, 'r')
            expression = file.readline().rstrip()
            file.close()
            operationOnIput(expression, sourceOfInput, path)
            
        elif(response == 3):
            break
        else:
            print("Choose from the given options!")


if __name__ == "__main__":
    main()
