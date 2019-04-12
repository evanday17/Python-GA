data_base = {  # create the dict of user names, pws and balances

    1000:
        {
            'Password': 'PW_1000',
            'Checking Balance': 5.00,
            'Savings Balance': 75.89,
        },
    1001:
        {
            'Password': 'PW_1001',
            'Checking Balance': 500.00,
            'Savings Balance': 1050.89,
        },
    1002:
        {
            'Password': 'PW_1002',
            'Checking Balance': 760.00,
            'Savings Balance': 3450.89,
        },
    1003:
        {
            'Password': 'PW_1003',
            'Checking Balance': 5000.00,
            'Savings Balance': 10500.89
        }

}

user_name = input('enter user name')
user_name = int(user_name)
pw = input('please enter pw')


if user_name in data_base:
    for values in data_base.values():
        if values['Password'] == pw:
            print('this worked')
else:
    print('no')


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

    def withdraw(self):  # take user input and subtract that from either the savings account or checkings accont
        print("How much would you like to withdraw?")