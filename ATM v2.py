#  the class is what is inside my bank and how to complete a transaction
#  the object is the transaction ?????????????????????????????


class Bank:
        def __init__(self,):

            self.data_base = {  # create the dict of user names, pws and balances

                "John_123":
                {
                    'Password': 'PW_1000',
                    'Checking Balance': 5.00,
                    'Savings Balance': 75.89,
                    },

                'Joe_456':
                {
                    'Password': 'PW_1001',
                    'Checking Balance': 500.00,
                    'Savings Balance': 1050.89,
                },

                'Billy_789':
                {
                    'Password': 'PW_1002',
                    'Checking Balance': 760.00,
                    'Savings Balance': 3450.89,
                    },

                'Nick_000':
                {
                    'Password': 'PW_1003',
                    'Checking Balance': 5000.00,
                    'Savings Balance': 10500.89
                }

            }
            print("Hello, Welcome to the ATM")
            self.user_validation = input("Please enter your username")
            self.password_validation = input('Please enter your password')

            while True:
                if self.user_validation in self.data_base:  # checks to see that the user name in in the dict
                    for values in self.data_base.values():  # iterates through the values
                        if values['Password'] == self.password_validation:  # if the value of pw is == user input...start program
                            print('Great, welcome ', self.user_validation)
                            print('How can I help you today?')
                            print()
                            print()
                            print('To check your savings balance: Press S')
                            print('To check your checkings balance: Press C')
                            print('To deposit money: Press D')
                            print('To withdrawal money: Press W')
                            print('To exit: Press E')
                else:
                    print("You entered an invalid user name and/or password")

                def savings_balance(self):
                    for keys, values in self.data_base.items():
                        for k, v in values.items():
                            if keys == self.user_validation:
                                if k == 'Savings Balance':
                                    print(v)

                def checkings_balance(self):  # print the checkings balance
                    pass

                def deposit(self):  # add deopsit to either the checkings or savings account
                    pass

                def withdraw(
                        self):  # take user input and subtract that from either the savings account or checkings accont
                    print("How much would you like to withdraw?")

                self.user_input = input('Please select an option')

                if self.user_input == 'C':
                    checkings_balance()

                elif self.user_input == 'S':
                    savings_balance(self)

                elif self.user_input == 'D':
                    deposit()

                elif self.user_input == 'W':
                    withdraw()

                elif self.user_input == 'E':
                    exit()

                else:
                    print('You enter an invalid selection')


def main():
    chase = Bank()



if __name__ == '__main__':
    main()