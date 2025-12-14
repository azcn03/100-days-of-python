# # # import another_module
# # # print(another_module.another_variable)
# # #from turtle

# # #imported the specified part of the module turtle


# # from turtle import Turtle, Screen
# # timmy = Turtle()
# # print(timmy)

# # timmy.shape("turtle")

# # timmy.color("blue")

# # timmy.fd(100)
# # my_screen = Screen()
# # print(my_screen.canvheight)

# # my_screen.exitonclick()

# import prettytable

# table = prettytable.PrettyTable()

# #couldn't change alignement before inserting values table.align = "l"

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
# table.align = "l"

# print(table)
#------------------------------Coffee Maker OOP---------------------------------

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

the_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_input = input(f"What would you like? ({the_menu.get_items()}): ")

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()

    elif the_menu.find_drink(user_input) is not None: 
        menu_item = the_menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)

    

        

