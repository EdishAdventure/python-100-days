

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract, 
    "*":multiply, 
    "/":divide}

def calculator():
    should_accumulate = True

    n1 = float(input("What is the first number? "))

    while should_accumulate == True:
        for symbol in operations:
            print(symbol)

        op = input("Pick an operation: ")
        n2 = float(input("What is the second number? "))

        result = operations[op](n1, n2)

        print(f"{n1} {op} {n2} = {result}")

        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to have a new calculation: ")

        if continue_calculation == "y":
            n1 = result
        else:
            should_accumulate = False
            print("Starting a new calculation...")
            calculator()

calculator()