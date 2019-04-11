# use a class
# ask for user name and password
# need main function


class Bank:

    def savings_balance(self):  # print the savings balance
        for keys, values in data_base.items():
            print(keys, values)

    def checkings_balance(self):  # print the checkings balanc
        pass

    def deposit(self):  # add deopsit to either the checkings or savings account
        pass

    def withdrawal(self):  # take user input and subtract that from either the savings account or checkings accont
        pass

    while True:
        print("Hello, Welcome to the ATM")

        user_validation = input("Please enter your username")
        password_validation = input('Please enter your password')

        if user_validation in data_base:  # checks to see that the user name in in the dict
            for values in data_base.values():  # iterates through the values
                if values['Password'] == password_validation:  # if the value of pw is == user input...start program
                    print('Great, welcome ', user_validation, ' How can i help you today?')
                    print('To check your savings balance: Press C')
                    print('To check your checkings balance: Press S')
                    print('To deposit money: Press D')
                    print('To withdrawal money: Press W')
                    print('To exit: Press E')

                    user_input = input('Please select an option')
                    if user_input == 'C':
                        checkings_balance()

                    elif user_input == 'S':
                        savings_balance()

                    elif user_input == 'D':
                        deposit()

                    elif user_input == 'W':
                        withdrawal()

                    elif user_input == 'E':
                        exit()

                    else:
                        print('You enter an invalid selection')

        else:
            print("You entered an invalid user name and/or password")
