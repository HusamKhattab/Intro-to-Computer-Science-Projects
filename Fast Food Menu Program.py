Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ef displayMenu():
    # Print menu
    print("MacDoogle’s:\n1. Hamburger = $1.50\n2. Soda = $1.15\n3.Fries = $1.25\n4. Complete Order")
    option = int(input()); # Take user input
    if option in [1, 2, 3, 4]: #Check if option is in range. If yes, return option else 0
        return option
    else:
        return 0

def quantityInput(itemselected):

    # Ask user to enter quantity a/c to item selected
    if itemselected == 1:
        quantity = int(input("Enter number of Hamburgers: "))
    elif itemselected == 2:
        quantity = int(input("Enter Number of Sodas :"))

    elif itemselected == 3:
        quantity = int(input("Enter Number of Fries:"))

    return quantity # return quantity


def calculateSubtotal(price, quantity):
    # multiply price and quantiyt and return
    return price * quantity


def calculateTax(subtotal):
    # calculate tax and return
    return subtotal * 0.10


def reciept(subtotal, tax, numberofitems):

    # print al the values
    print("Subtotal: $", "{0:.2f}".format(subtotal))
    print("Tax: $", "{0:.2f}".format(tax))
    print("Total cost: $", "{0:.2f}".format(subtotal + tax))
    print("Number of items: ", numberofitems)
    print("Enjoy Your Meal!")


if __name__ == "__main__":
    option = displayMenu(); # store return option value
    while (option == 0): # ask user to enter option again if value is invalid else go further
        print("Enter valid option!!")
        option = displayMenu();
    numberofitems = 0
    total = 0

    # iterate the loop until user enters 4
    while True:
        if option == 1:
            quantity = quantityInput(option) # get quantity
            numberofitems += quantity # add quantity to number of items
            total += calculateSubtotal(1.50, quantity) # calculate total for current item and add to total
            option = displayMenu(); # display menu again
        elif option == 2:
            quantity = quantityInput(option)
            numberofitems += quantity
            total += calculateSubtotal(1.15, quantity)
            option = displayMenu();
        elif option == 3:
            quantity = quantityInput(option)
            numberofitems += quantity
            total += calculateSubtotal(1.25, quantity)
            option = displayMenu();
        elif option == 4:
            tax = calculateTax(total) # calculate tax on total
            reciept(total, tax, numberofitems) # call reciept method to display reciept and terminate loop
            break;
