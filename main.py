from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu = Menu()
# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
#
# is_on = True
# while is_on:
#     option = menu.get_items()
#     choice = input(f"Enter Your Choice {option}")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else :
#         drink = menu.find_drink(choice)
#         if  coffee_maker.is_resource_sufficient(drink):
#             if money_machine.make_payment(drink.cost):
#                 coffee_maker.make_coffee(drink)

menu = Menu()
options = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True
while on:
    choice = input(f"Enter Your Choice {options}")
    if choice == "off":
        on = False
    elif choice == "report" :
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        cost = drink.cost
        print(f"Cost = {cost}")
        # money_machine.process_coins()
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(cost) :
                coffee_maker.make_coffee(drink)



