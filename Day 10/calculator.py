from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    continue_calculating = True

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an Operation: ")

        next_number = float(input("What's the next number?: "))

        answer = float(operations[operation](first_number, next_number))

        print(f"{first_number} {operation} {next_number} = {answer}")
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new "
                                     f"calculation: ").lower()
        if continue_calculation == 'n':
            continue_calculating = False
            print("\n" * 25)
            calculator()
        else:
            first_number = answer

calculator()