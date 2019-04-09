products = {
    "Milk" : 5,
    "Steak" : 35,
    "Eggs" : 6.33,
    "Bread" : 12.50
}

shopping_bag = []
discounts = []


def add_to_bag(): # ask the user what they want to add to the bag and then add it to our shopping bag
    enter_product = input("What would you like to add to your bag?")
    shopping_bag.append(enter_product)
    print(shopping_bag)

def apply_discounts():
