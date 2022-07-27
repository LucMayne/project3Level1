# import tabulate to format data
from tabulate import tabulate

class Shoes:
    # init variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # returns the price of a shoe
    def get_cost(self):
        return self.cost
    
    # returns the quantity of a shoe
    def get_quanty(self):
        return self.quantity

    # returns formatted list
    def __str__(self):
        shoe_info = [[self.country], [self.code], [self.product], [self.cost], [self.quantity]]
        return tabulate(shoe_info)

# list to store each Shoes object
shoe_list = []
fist_line = "Country,Code,Product,Cost,Quantity"

def read_shoes_data():    

    """Save text from inventory.txt to content_list
        Create a shoe object for each shoe in content_list
        Append shoe to shoe_list.
    """

    with open("inventory.txt", "r+") as inven_file:
        content = inven_file.readlines()
        # remove the first line of the file
        content.pop(0)

    # save file contents
    content_list = [line.strip().split(',') for line in content]

    # loop over each item
    for item in content_list:     
        country = item[0]
        code = item[1]
        product = item[2]
        cost = item[3]
        quantity = item[4]

        # create a shoe object and append
        shoe = Shoes(country, code, product, cost, quantity)
        shoe_list.append(shoe)

def capture_shoes():
    """Ask user for info
        Create a new shoe object
        Append shoe to shoe_list
        Write to inventory.txt.
    """
    # get info from user
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")

    # create new Shoes object
    shoe = Shoes(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    # write updated data to to inventory.txt
    with open("inventory.txt", "w") as new_inven:
        # add first line back
        new_inven.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            new_inven.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    
def view_all():
    # prints info for each shoe
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    """Find shoe with the least quantity
        Ask user if they want to restock
        If yes, ask for a new quantity and update that shoe object
        Write new data to inventory.txt.
    """
    # quantity, quantity index
    quant = 0
    quant_index = 0

    for index, shoe in enumerate(shoe_list):
        # on first iteration set quant to first quantity value
        if index == 0:
            quant = int(shoe.quantity)
        # if shoe.quantity is less than quant, update quant and quant_index
        if int(shoe.quantity) < quant:
            quant = int(shoe.quantity)
            quant_index = index
    
    print(f"Shoe with least stock: {shoe_list[quant_index].product}, Stock: {quant}")
    # ask user if they want to update the quantity
    add_quant = input("Would you like to restock this item (Y/N): ").upper()

    if add_quant == 'Y':
        # ask for new quantity
        new_quant = int(input("Enter the quantity: "))
        # update shoe_list
        shoe_list[quant_index].quantity = new_quant
        
        # write updated data to to inventory.txt
        with open("inventory.txt", "w") as new_inven:
            # add first line back
            new_inven.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                new_inven.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

        print("Updated shoe list.")
    
    elif add_quant == 'N':
        pass
    else:
        print("\nWrong input!")

def search_shoe():
    # ask user for code
    code = input("Shoe code: ")
    # print shoe info if the code is in the list
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)

def value_per_item():
    # prints total value of each item in the list
    for shoe in shoe_list:
        value = (int(shoe.cost) * int(shoe.quantity))
        print(f"Total value of {shoe.product}'s: R{value}")

def highest_qty():
    # prints the shoe with the highest quantity
    quant = 0
    quant_index = 0

    # loop over shoe_list
    for index, shoe in enumerate(shoe_list):
        # update quant if current value is greater than the last
        if int(shoe.quantity) > quant:
            quant = int(shoe.quantity)
            quant_index = index
    
    print(f"\n{shoe_list[quant_index].product} is on sale!")

def main():
    # call function to update shoe_list
    read_shoes_data()

    while True:
        # ask user to select one of the options
        user_choice = input("""\nSelect one of the options below:
as - Add shoe
va - View all
rs - Restock
ss - Search for a shoe
sv - Shoe value
hq - Print shoe with highest quantity 
e  - Exit
: """).lower()

        if user_choice == 'as':
            capture_shoes()
        elif user_choice == 'va':
            view_all()
        elif user_choice == 'rs':
            re_stock()
        elif user_choice == 'ss':
            search_shoe()
        elif user_choice  == 'sv':
            value_per_item()
        elif user_choice == 'hq':
            highest_qty()
        elif user_choice == 'e':
            break
        else:
            print("\nWrong input!")

# call main function
main()
