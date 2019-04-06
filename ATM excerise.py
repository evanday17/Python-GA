# use a class
# ask for user name and password
# need main function
class Bank:


    data_base = { # create the dict of user names, pws and balances

        1000:
            {
                'User Name': 'User 1000',
                'Password': 'PW_1000',
                'Checking Balance': 5.00,
                'Savings Balance': 75.89,
            },
        1001:
            {
                'User Name': 'User 1001',
                'Password': 'PW_1001',
                'Checking Balance': 500.00,
                'Savings Balance': 1050.89,
            },
        1002:
            {
                'User Name': 'User 1002',
                'Password': 'PW_1002',
                'Checking Balance': 760.00,
                'Savings Balance': 3450.89,
            },
        1003:
            {
                'User Name': 'User 1003',
                'Password': 'PW_1003',
                'Checking Balance': 5000.00,
                'Savings Balance': 10500.89
            }

    }

    for keys, values in data_base.items():
        for k, y in values.items():
            print(k, ':', y)
