from importlib.resources import is_resource

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
while is_on:
    choice = input(f"What would you like to drink {menu.get_items()}?: ")

    if choice == "off":
        is_on = False
        continue
    if choice == "report":
        money_machine.report()
        coffee_maker.report()
        continue
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    print()