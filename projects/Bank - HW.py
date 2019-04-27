import datetime

date = datetime.date.today().isoformat()

class BankTeller:
    def __init__(self):

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
                            pass
                            break  # i know we aren't suppose to use breaks but not sure how else to do this?
                            # if i don't break it will loop through all of the k's and v's
                        else:
                            print('You entered the wrong password')
                            print('-------------------------------------------------------------------------------')
                            self.password = input('Please enter your pw again')
                            if keys == self.account_number and values["Password"] == self.password:
                                print('Welcome,', values["Name"], 'I was able to confirm your account info')
                                break
                            else:
                                print('We cannot confirm your password')
                                print('Goodbye')
                                exit()
                # this else statement isn't working and i'm not sure why
                else:
                    print("The account is not in our system")
                    self.account_number = input('Please enter your # again')
                    if self.account_number in self.accounts:
                        for keys, values in self.accounts.items():
                            if keys == self.account_number and values["Password"] == self.password:
                                print('Welcome,', values["Name"], 'I was able to confirm your account info')
                                print('-------------------------------------------------------------------------------')
                                print('-------------------------------------------------------------------------------')
                                break  # i know we aren't suppose to use breaks but not sure how else
                    else:
                        print('We still cannot find your account, goodbye')
                        exit()

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
                        for keys, values in self.accounts.items():
                            for k, v in values.items():
                                if k == 'Transaction Log':
                                    values['Transaction Log'].append({date: {'Savings Account': -amount}})
                        print('We have sent', amount, 'over to account:', to_account)
                        print('Your new balance is', values['Savings Balance'])
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        for keys, values in self.accounts.items():
                            if keys == to_account:
                                new_transfer_balance = float(amount) + values['Savings Balance']
                                values['Savings Balance'] = new_transfer_balance
                                # created a dict inside my transaction list...adds +log to the receiving account
                                for keys, values in self.accounts.items():
                                    for k, v in values.items():
                                        if k == 'Transaction Log':
                                            values['Transaction Log'].append({date: {'Savings Account': amount}})


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
                        for keys, values in self.accounts.items():
                            for k, v in values.items():
                                if k == 'Transaction Log':
                                    values['Transaction Log'].append({date: {'Checking Account': -amount}})
                        print('We have sent', amount, 'over to account:', to_account)
                        print('Your new balance is', values['Checking Balance'])
                        print('-------------------------------------------------------------------------------')
                        print('-------------------------------------------------------------------------------')
                        for keys, values in self.accounts.items():
                            if keys == to_account:
                                new_transfer_balance_2 = float(amount) + values['Checking Balance']
                                values['Checking Balance'] = new_transfer_balance_2
                                # created a dict inside my transaction list...adds +log to the receiving account
                                for keys, values in self.accounts.items():
                                    for k, v in values.items():
                                        if k == 'Transaction Log':
                                            values['Transaction Log'].append({date: {'Checking Account': amount}})


        else:
            print('That account dose not exist')
            print('Goodbye')
            exit()


class Customer(BankTeller):
    def __init__(self):
        super().__init__()

    def check_savings_balance(self, account_number):
        try:
            self.account_number= account_number

        except ValueError:
            print('Account number must contain numbers only')

        except Exception as e:
            print(e)

        else:
            for keys, values in self.accounts.items():
                if keys == self.account_number:
                    print('-------------------------------------------------------------------------------')
                    print('-------------------------------------------------------------------------------')
                    print('There is a total of ', values['Savings Balance'], 'in your savings account')
                    print('-------------------------------------------------------------------------------')
                    print('-------------------------------------------------------------------------------')
                else:
                    print("Sorry, something went wrong")


    def check_checking_balance(self, account_number_cb):
        self.account_number_cb = account_number_cb
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
                print_tl = input("would you like to print your log?")
                # this will print a text file of the transaction log
                if print_tl == 'Yes':
                    def write_file(f, text):
                        text_file = open(f, 'w') #  creates the text file
                        text_file.write(text)    # writes the data
                        return text_file

                    def read_file(f):  # need to format the data but i cannot for SOME REASONNNNNNNN
                        d= {}
                        file = open(f,'r')
                        for line in file:
                            col = line.split(',')  # split the data by ;
                            print(col)
                            return d

                    write_file('Transaction Log.txt', str(values['Transaction Log']))
                    read_file('Transaction Log.txt')
                    print("We have printed your logs")
                    break
                else:
                    print("Ok")
                    print('-------------------------------------------------------------------------------')
                    break


def main():

    print('Hello, welcome to the bank')
    print('Lets start by verifying your account and pw')

    try:
        user = int(input("Enter your Account #"))
    except ValueError:
        print('Account number must contain numbers only')

    except Exception as e:
        print(e)
    else:
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

        try:
            user_choice = input('')
        except ValueError:
            print('Account number must contain numbers only')

        except Exception as e:
            print(e)

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