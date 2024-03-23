# Create menu dic
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# set current price to 0
total = 0

# loop
while True:

    try:
        #user inut
        item = input("Item: ").title()
        #check if item is already in the dic
        if item in menu:
            # Add the item price to current price
            total += menu[item]
            format_total = "{:.2f}".format(total)
            #print the current price
            print(f"Total: ${format_total}")

    except EOFError:
        # print a new line and stop loop
        print()
        break