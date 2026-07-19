MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}

def process_coins():
    """Processes the inserted coins into tangible amount."""
    quarters = 0.25 * int(input("How many quarters ?: "))
    dimes = 0.10 * int(input("How many dimes ?: "))
    nickels = 0.05 * int(input("How many nickels ?: "))
    pennies = 0.01 * int(input("How many pennies ?: "))
    amount = quarters + dimes + nickels + pennies
    return amount

def check_resources(coffee):
    """Returns True or False after Checking are the resources present in the required quantity."""
    required_ingredients = MENU[f"{coffee}"]["ingredients"]
    for ingredient in required_ingredients:
        if resources[ingredient] < required_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

    
def check_transaction_status(amount, coffee):
    """Returns True or False based on the cost and amount"""
    cost = MENU[f"{coffee}"]["cost"]
    if amount < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True    

def update_resources(coffee, coffee_cost):
    """Updates the resources after a successful transaction"""
    required_ingredients = MENU[f"{coffee}"]["ingredients"]
    for ingredient in required_ingredients:   
        resources[ingredient] -= required_ingredients[ingredient]
    resources["Money"] += coffee_cost

def coffee_machine():
    command = input("What would you like? (espresso/latte/cappuccino):").lower()
    if command == "off":
        return
    elif command == "report":
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Coffee: {resources['coffee']}g ")
        print(f"Money: ${resources['Money']} ")

    else:
        amount_inserted = process_coins()
        if check_transaction_status(amount_inserted, command) and check_resources(command):
            cost = MENU[f"{command}"]["cost"]
            change = amount_inserted - cost
            update_resources(command, cost)
            print(f"Here is ${change:.2f} in change.")
            print(f"Here's is your {command}🍵. Enjoy!")
    coffee_machine()


coffee_machine()
