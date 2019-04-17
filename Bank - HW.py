
class BankTeller:
    def __init__(self,):

        self.accounts = {

            123: {
                "Password": 'hello',
                'Checking Balance': 5444.00,
                'Savings Balance': 15124.00,
                'Name': 'Jeff'
                },

            1234:
                {
                "Password": 'goodbye',
                "Checking Balance": 2345.30,
                "Savings Balance": 15432.04,
                "Name": 'Evan'
                },

            12345: {
                "Password": 'bye',
                "Checking Balance": 5.65,
                "Savings Balance": 15721.24,
                "Name": 'Nick'
                }
            }

    def greetings(self, account_number, password):

        try:
            self.account_number = float(account_number)
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
                        break  # i know we aren't suppose to use breaks but not sure how else to do this?
                        # if i don't break it will loop through all of the k's and v's
                    else:
                        print('You entered the wrong password')
            else:
                print("The Account/Password is invalid")

    def transfer(self, to_account, from_account,amount):
        self.to_account = to_account
        self.from_account = from_account
        self.amount = float(amount)

        # make sure we look up the right account and look through that dict
        for keys, values in self.accounts.items():
            if keys == self.account_number:
                total_amount = values['Checking Balance'] + values['Savings Balance']
                if total_amount < float(amount):  # make sure there is enough funds
                    print('-------------------------------------------------------------------------------')
                    print('-------------------------------------------------------------------------------')
                    print('You do not have enough money')
                    print('You only have ', total_amount, 'available between your 2 accounts')
                else:
                    # subtract transfer request....need to add new value to his dict
                    # also, need to add the transfer amount to requested account
                    new_balance = total_amount - float(amount)
                    print('-------------------------------------------------------------------------------')
                    print('-------------------------------------------------------------------------------')
                    print(new_balance, ' this should be the new balance')
            else:
                pass


class Customer:
    pass
#  need to have ability to check balance
# request transfer
# ask for withdrawl
# deposit $$$$

def main():

    first_user = BankTeller()
    first_user.greetings(123, 'hello')
    first_user.transfer('123','',100)

if __name__ == '__main__':
    main()