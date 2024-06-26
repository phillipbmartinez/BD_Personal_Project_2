# Food Ordering 

from prettytable import PrettyTable


drinks = {"d1": {"item_number": "d1", "calories": 150, "price": 1.50, "item_name": "Coke"},
          "d2": {"item_number": "d2","calories": 0, "price": 1.50, "item_name": "Diet Coke"},
          "d3": {"item_number": "d3", "calories": 0, "price": 0, "item_name": "Water"},
          "d4": {"item_number": "d4", "calories": 100, "price": 1, "item_name": "Juice"},
          "d5": {"item_number": "d5", "calories": 0, "price": 0, "item_name": "No Drink"},}

sandwiches = {"s1": {"item_number": "s1", "calories": 500, "price": 7, "item_name": "Burger"},
              "s2": {"item_number": "s2", "calories": 450, "price": 4, "item_name": "BLT"},
              "s3": {"item_number": "s3", "calories": 300, "price": 5, "item_name": "Turkey"},
              "s4": {"item_number": "s4", "calories": 300, "price": 5, "item_name": "Veggie"},
              "s5": {"item_number": "s5", "calories": 0, "price": 0, "item_name": "No Sandwich"},}

sides = {"ss1": {"item_number": "ss1", "calories": 150, "price": 1, "item_name": "Chips"},
         "ss2": {"item_number": "ss2","calories": 50, "price": 1.50, "item_name": "Apple"},
         "ss3": {"item_number": "ss3", "calories": 300, "price": 1.50, "item_name": "Fries"},
         "ss4": {"item_number": "ss4", "calories": 25, "price": 1, "item_name": "Celery"},
         "ss5": {"item_number": "ss5", "calories": 0, "price": 0, "item_name": "No Side"},}

desserts = {"dd1": {"item_number": "dd1", "calories": 500, "price": 1, "item_name": "Ice Cream"},
            "dd2": {"item_number": "dd2", "calories": 300, "price": 1, "item_name": "Brownie"},
            "dd3": {"item_number": "dd3", "calories": 300, "price": 1, "item_name": "Cookie"},
            "dd4": {"item_number": "dd4", "calories": 200, "price": 1, "item_name": "Sherbert"},
            "dd5": {"item_number": "dd5", "calories": 0, "price": 0, "item_name": "No Dessert"},}

menu = PrettyTable(["Menu Item #", "Menu Item", "Price", "Calories"])
menu.add_row([drinks["d1"]["item_number"], drinks["d1"]["item_name"], f"${drinks['d1']['price']}", drinks["d1"]["calories"]])
menu.add_row([drinks["d2"]["item_number"], drinks["d2"]["item_name"], f"${drinks['d2']['price']}", drinks["d2"]["calories"]])
menu.add_row([drinks["d3"]["item_number"], drinks["d3"]["item_name"], f"${drinks['d3']['price']}", drinks["d3"]["calories"]])
menu.add_row([drinks["d4"]["item_number"], drinks["d4"]["item_name"], f"${drinks['d4']['price']}", drinks["d4"]["calories"]])
menu.add_row(["*****","*****", "*****", "*****"])

menu.add_row([sandwiches["s1"]["item_number"], sandwiches["s1"]["item_name"], f"${sandwiches['s1']['price']}", sandwiches["s1"]["calories"]])
menu.add_row([sandwiches["s2"]["item_number"], sandwiches["s2"]["item_name"], f"${sandwiches['s2']['price']}", sandwiches["s2"]["calories"]])
menu.add_row([sandwiches["s3"]["item_number"], sandwiches["s3"]["item_name"], f"${sandwiches['s3']['price']}", sandwiches["s3"]["calories"]])
menu.add_row([sandwiches["s4"]["item_number"], sandwiches["s4"]["item_name"], f"${sandwiches['s4']['price']}", sandwiches["s4"]["calories"]])
menu.add_row(["*****","*****", "*****", "*****"])

menu.add_row([sides["ss1"]["item_number"], sides["ss1"]["item_name"], f"${sides['ss1']['price']}", sides["ss1"]["calories"]])
menu.add_row([sides["ss2"]["item_number"], sides["ss2"]["item_name"], f"${sides['ss2']['price']}", sides["ss2"]["calories"]])
menu.add_row([sides["ss3"]["item_number"], sides["ss3"]["item_name"], f"${sides['ss3']['price']}", sides["ss3"]["calories"]])
menu.add_row([sides["ss4"]["item_number"], sides["ss4"]["item_name"], f"${sides['ss4']['price']}", sides["ss4"]["calories"]])
menu.add_row(["*****","*****", "*****", "*****"])

menu.add_row([desserts["dd1"]["item_number"], desserts["dd1"]["item_name"], f"${desserts['dd1']['price']}", desserts["dd1"]["calories"]])
menu.add_row([desserts["dd2"]["item_number"], desserts["dd2"]["item_name"], f"${desserts['dd2']['price']}", desserts["dd2"]["calories"]])
menu.add_row([desserts["dd3"]["item_number"], desserts["dd3"]["item_name"], f"${desserts['dd3']['price']}", desserts["dd3"]["calories"]])
menu.add_row([desserts["dd4"]["item_number"], desserts["dd4"]["item_name"], f"${desserts['dd4']['price']}", desserts["dd4"]["calories"]])

print(menu)


print("Welcome!")
drink_choice = input("What would you like to drink? ")
sandwich_choice = input("What sandwich would you like? ")
side_choice = input("Would you like a side dish? ")
dessert_choice = input("What about dessert? ")

total_calories = drinks[drink_choice]["calories"] + sandwiches[sandwich_choice]["calories"] + sides[side_choice]["calories"] + desserts[dessert_choice]["calories"]
total_cost = drinks[drink_choice]["price"] + sandwiches[sandwich_choice]["price"] + sides[side_choice]["price"] + desserts[dessert_choice]["price"]

print(f"The total number of calories for your meal is: {total_calories}")
print(f"The total cost of your meal is: ${total_cost}0")
print("\n")

ordering = True
continue_ordering = input("Would you like to add to this order? ")
while ordering:
    if continue_ordering == "No":
        ordering = False
        print("Thank you, have a great day.")
    elif continue_ordering == "Yes":
        drink_choice = input("What would you like to drink? ")
        sandwich_choice = input("What sandwich would you like? ")
        side_choice = input("Would you like a side dish? ")
        dessert_choice = input("What about dessert? ")
        total_calories += drinks[drink_choice]["calories"] + sandwiches[sandwich_choice]["calories"] + sides[side_choice]["calories"] + desserts[dessert_choice]["calories"]
        total_cost += drinks[drink_choice]["price"] + sandwiches[sandwich_choice]["price"] + sides[side_choice]["price"] + desserts[dessert_choice]["price"]
        continue_ordering = input("Would you like to add to this order? ")
        if continue_ordering == "No":
                ordering = False
                print("\n")
                print(f"The total number of calories for your meal is now: {total_calories}")
                print(f"The total cost of your meal is now: ${total_cost}0")
