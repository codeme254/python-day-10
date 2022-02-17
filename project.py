
# calculator
def add(n1, n2):
    """Takes in two numbers and returns their sum"""
    return n1 + n2

def subtract(n1, n2):
    """Takes in two numbers and returns their difference"""
    return n1 - n2

def multiply(n1, n2):
    """Takes in two numbers and returns their product"""
    return n1 * n2

def divide(n1, n2):
    """Takes in two numbers and returns their division result"""
    return n1 / n2

# dictionary called operations where the keys are the operators and the values are the names of the functions above
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)

    continuing = True
    while continuing:
        opration_symbol = input("Pick an operation symbol from the line above: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[opration_symbol](num1, num2)
        print(f"{num1} {opration_symbol} {num2} = {answer}")

        looping = input(f"Type 'y' to continue calculating with {answer} or 'n to start a new calculation': ")
        if looping == 'y':
            num1 = answer
        else:
            calculator()
calculator()