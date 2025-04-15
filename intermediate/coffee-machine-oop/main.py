from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_on:
    user_choice = input(f"What would you like?({menu.get_items()}): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif menu.find_drink(user_choice):
        coffee = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_machine.make_coffee(coffee)
