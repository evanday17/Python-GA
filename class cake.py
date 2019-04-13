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
        if values['Savings Balance'] == pw:
            print('this worked')
else:
    print('no')
