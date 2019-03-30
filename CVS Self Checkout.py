product = []
price = []
discount_amount = []

while True:
    print("========== Hello, Please Begin The Checkout ==========")
    print('To Enter A Product Press: P')
    print('To Enter A Discount Amount Press: D')
    print('To Remove item Press: R')
    print('Check List: L')
    print('Check Total: T')
    print('Finish Checkout: F')
    print('Exit: E')

    enter_choice = input('***Please select a choice***') # get user choice

    if enter_choice == 'P':
        enter_product = input("what product are you purchasing?")
        enter_price = int(input("how much is it?"))
        product.append(enter_product)
        price.append(enter_price)

    elif enter_choice == 'E':
        exit()

    elif enter_choice == 'D':
        enter_discount = int(input("please enter discount amount"))
        discount_amount.append(enter_discount)

    elif enter_choice == 'T':
        print('***Your total so far is ',(sum(price)),'***')
        print('Please note: This is not including sales tax')

    elif enter_choice == 'L':
        print(product)

    elif enter_choice == 'F':
        total = (sum(price) - sum(discount_amount))
        final_total = (total * .07) + total
        print('***After applying a discount of ', discount_amount ,' your final total is ', final_total, '***')
        print('You purchased the following...')
        print(product, price)
        exit()

    elif enter_choice == "R":
        print('So far you have selected the following...')
        print(product)
        remove_item = input("Which would you like to remove")
        if remove_item in product:
            product.remove(remove_item)
            print('Item Removed...Here is your new list:')
            print(product) # need to remove the price fromt he list as well as the item
        else:
            print("Ok, got it")


    else:
        print('invalid choice')

