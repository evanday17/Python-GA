# use a class
# ask for user name and password
# need main function


class Bank:

    while True:

        data_base = {  # create the dict of user names, pws and balances

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

        def savings_balance(self):
            pass

        def checkings_balance(self):
            pass

        def deposit(self):
            pass

        def withdrawal(self):
            pass

        print("Hello, Welcome to the ATM")

        user_validation = input("Please enter your username")
        password_validation = input('Please enter your password')

        if user_validation in data_base: # checks to see that the user name in in the dict
            for values in data_base.values(): # iterates through the values
                if values['Password'] == password_validation: # if the value of pw is == user input...start program
                    print('Great, welcome ', user_validation, ' How can i help you today?')
                    print('Check Savings Balance: Press C')
                    print('Check Checkings Balance: Press S')
                    print('Deposit Money: Press D')
                    print('Withdrawal: Press W')
                    print('Exit: Press E')

        else:
            print('You entered an invalid user name and/or password')

