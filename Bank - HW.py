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
                        print('Welcome,', values["Name"], 'I was able to confirm your account info')
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        break  # i know we aren't suppose to use breaks but not sure how else to do this?
                        # if i don't break it will loop through all of the k's and v's
                    else:
                        print('You entered the wrong password')
            else:
                print("The Account/Password is invalid")

    def transfer(self, to_account, from_account,amount, what_account):  # just need to add a transaction log to this
        self.to_account = to_account # what account are we transferring to
        self.from_account = from_account
        self.amount = float(amount) # transfer amount
        self.what_account = what_account  # what account are we transferring from, checkings or savings?

#  If Checkings is selected...make sure there is enough money and if so, complete the transfer
        if what_account == 'Savings Balance':

            for keys, values in self.accounts.items():
                if keys == self.account_number:
                    if values['Savings Balance'] < float(amount):
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        print('Sorry, but you do not have enough money to transfer')
                        print('You only have', values['Savings Balance'], ' in your account')
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')

                    else:
                        new_balance = values['Savings Balance'] - float(amount)
                        values['Savings Balance'] = new_balance  # update savings balance
                        print('-------------------------------------------------------------------------------')
                        print('Great, your transfer has been complete')
                        print('-------------------------------------------------------------------------------')
                        values['Transaction Log'].append({'Savings Account': -amount})  # adds to trans log
                        print('We have sent', amount, 'over to account:', to_account)
                        print('Your new balance is', values['Savings Balance'])
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        for keys, values in self.accounts.items():
                            if keys == to_account:
                                new_transfer_balance = float(amount) + values['Savings Balance']
                                values['Savings Balance'] = new_transfer_balance
                                # created a dict inside my transaction list...adds +log to the receiving account
                                values['Transaction Log'].append({'Savings Account': amount})

#  If Checkings is selected...make sure there is enough money and if so, complete the transfer
        elif what_account == 'Checking Balance':
            for keys, values in self.accounts.items():
                if keys == self.account_number:
                    if values['Checking Balance'] < float(amount):
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        print('Sorry, but you do not have enough money to transfer')
                        print('You only have', values['Checking Balance'], ' in your account')
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')

                    else:
                        new_balance = values['Checking Balance'] - float(amount)
                        values['Checking Balance'] = new_balance  # update savings balance
                        print('Great, your transfer has been complete')
                        values['Transaction Log'].append({'Checking Account': -amount})  # adds to trans log
                        print('We have sent', amount, 'over to account:', to_account)
                        print('Your new balance is', values['Checking Balance'])
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        for keys, values in self.accounts.items():
                            if keys == to_account:
                                new_transfer_balance_2 = float(amount) + values['Checking Balance']
                                values['Checking Balance'] = new_transfer_balance_2
                                # created a dict inside my transaction list...adds +log to the receiving account
                                values['Transaction Log'].append({'Checking Account': amount})

        else:
            print('That account dose not exist')
            print('Goodbye')
            exit()


class Customer(BankTeller):
    def __init__(self):
        super().__init__()

    def check_savings_balance(self, account_number):
        self.account_number= account_number
        for keys, values in self.accounts.items():
            if keys == self.account_number:
                print('-------------------------------------------------------------------------------')
                print('-------------------------------------------------------------------------------')
                print('There is a total of ', values['Savings Balance'], 'in your savings account')
                print('-------------------------------------------------------------------------------')
                print('-------------------------------------------------------------------------------')


    def check_checking_balance(self, account_number_cb):
        self.account_number_cb= account_number_cb
        for keys, values in self.accounts.items():
            if keys == self.account_number:
                print('-------------------------------------------------------------------------------')
                print('-------------------------------------------------------------------------------')
                print('There is a total of ', values['Checking Balance'], 'in your savings account')
                print('-------------------------------------------------------------------------------')
                print('-------------------------------------------------------------------------------')

    def check_tl(self, tl):
        self.tl= tl
        for keys, values in self.accounts.items():
            if keys == self.account_number:
                print('-------------------------------------------------------------------------------')
                print('-------------------------------------------------------------------------------')
                print('Here is a list of all of your transactions')
                print(values["Transaction Log"])
                print('-------------------------------------------------------------------------------')
                print('-------------------------------------------------------------------------------')


def main():

    print('Hello, welcome to the bank')
    print('Lets start by verifying your account and pw')
    user = int(input("Enter your Account #"))
    pw = input('Enter your password')
    first_user = Customer()
    first_user.greetings(user, pw)

    while True:

        print('Please select one of the below options')
        print('-----Check Savings Account Balance: SB')
        print('-----Check Checkings Account Balance: CB')
        print('-----Transfer: T')
        print('-----Check Transaction Log: TL')
        print('-----Exit: E')

        user_choice = input('')

        if user_choice == 'T':
            account_recieve = int(input('Enter the account # you are sending to'))
            own_account = int(input('Please re-enter your account #'))
            t_amount = int(input('How much do you want to transfer?'))
            account_type = input('Which acount are you transfering from: Checkings or Saving')
            first_user.transfer(account_recieve, own_account, t_amount, account_type)
        
        elif user_choice == 'CB':
            first_user.check_checking_balance(user)
    
        elif user_choice == 'SB':
            first_user.check_savings_balance(user)
    
        elif user_choice == 'TL':
            first_user.check_tl(user)

        elif user_choice == 'E':
            exit()
        else:
            print('You entered an invalid selection')


if __name__ == '__main__':
    main()