
class BankTeller:
    def __init__(self,):

        self.accounts = {

            123: {
                "Password": 'hello',
                'Checking Balance': 5444.00,
                'Savings Balance': 15124.00,
                'Name': 'Jeff',
                'Transaction Log': []
                },

            1234:
                {
                "Password": 'goodbye',
                "Checking Balance": 2345.30,
                "Savings Balance": 15432.04,
                "Name": 'Evan',
                'Transaction Log': []
                },

            12345: {
                "Password": 'bye',
                "Checking Balance": 5.65,
                "Savings Balance": 15721.24,
                "Name": 'Nick',
                'Transaction Log': [],
                }
            }

    def greetings(self, account_number, password):  # validate that the account is in our system

        try:
            self.account_number = account_number  # why does this work
            self.password = password

        except ValueError:
            print('Account number must contain numbers only')

        except Exception as e:
            print(e)

        else:
            if self.account_number in self.accounts:
                for keys, values in self.accounts.items():
                    if keys == self.account_number and values["Password"] == self.password:
                        print('Welcome,', values["Name"])
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        break  # i know we aren't suppose to use breaks but not sure how else to do this?
                        # if i don't break it will loop through all of the k's and v's
                    else:
                        print('You entered the wrong password')
            else:
                print("The Account/Password is invalid")



class Customer(BankTeller):
    def __init__(self):
        super().__init__()





def main():
    pw = input('what is your pw')
    u = int(input('what is your username'))
    first_user = Customer()
    first_user.greetings(u, pw)






    '''first_user = Customer()
    first_user.greetings('hello')
    first_user.transfer(1234,'123',1000,'Savings Balance')'''

if __name__ == '__main__':
    main()