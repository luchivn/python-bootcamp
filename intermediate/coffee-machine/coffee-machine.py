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

machine_on = True
enough_resources = True
money = 0

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money}$")
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        for resource in MENU[user_choice]['ingredients']:
            if MENU[user_choice]['ingredients'][resource] > resources[resource]:
                print(f"Sorry there is not enough {resource}")
                enough_resources = False
        if enough_resources:
            print("Insert coins 🪙")
            quarters = int(input("quarters: "))
            dimes = int(input("dimes: "))
            nickles = int(input("nickles: "))
            pennies = int(input("pennies: "))
            total = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
            if total < MENU[user_choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif total >= MENU[user_choice]['cost']:
                money += MENU[user_choice]['cost']
                change = total - MENU[user_choice]['cost']
                for resource in MENU[user_choice]['ingredients']:
                    resources[resource] -= MENU[user_choice]['ingredients'][resource]
                if change:
                    print(f"Here is ${round(change,2)} dollars in change.")
                print(f"Here is your {user_choice}☕ Enjoy!")
        else:
            print('Try getting another coffee')
    else:
        print("Invalid input. Try again.")
