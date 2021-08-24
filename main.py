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
}


money_deposit = 0


def check_resources(drink):

    flag = 0
    if MENU[drink]['ingredients']['water'] < resources['water']:
        pass
    else:
        print("Sorry there is not enough water")
        flag = 1

    if drink != 'espresso':
        if MENU[drink]['ingredients']['milk'] < resources['milk']:
            pass
        else:
            print("Sorry there is not enough milk")
            flag = 1

    if MENU[drink]['ingredients']['coffee'] < resources['coffee']:
        pass
    else:
        print("Sorry there is not enough coffee")
        flag = 1

    return flag


def calculate_resource(drink):
    global money_deposit
    resources['water'] -= MENU[drink]['ingredients']['water']

    if drink != 'espresso':
        resources['milk'] -= MENU[drink]['ingredients']['milk']

    resources['coffee'] -= MENU[drink]['ingredients']['coffee']

    money_deposit += MENU[drink]['cost']


def drink(drink_name, coins_inserted):

    change = 0

    if MENU[drink_name]['cost'] == coins_inserted:
        calculate_resource(drink_name)
        print(f"Here is your {drink_name}. Enjoy!")
    elif coins_inserted > MENU[drink_name]['cost']:
        calculate_resource(drink_name)
        change = coins_inserted - MENU[drink_name]['cost']
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink_name}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def machine_report(amount):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${amount}")


user_drink = ''
total_amount_paid = 0

while user_drink != 'off':
    user_drink = input("What would you like? (espresso/late/cappuccino): ").lower()

    if user_drink == 'latte' or user_drink == 'espresso' or user_drink == 'cappuccino':
        result = check_resources(user_drink)

        if result == 0:
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_amount_paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            drink(user_drink, round(total_amount_paid, 2))
    elif user_drink == 'report':
        machine_report(round(money_deposit, 2))
