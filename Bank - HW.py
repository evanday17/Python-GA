
class BankTeller:
    def __init__(self):

        self.accounts = {
            123: {
                "Password": 'hello',
                'Checking Balance': 5444.00,
                'Savings Balance': 15124.00
                },

            1234:{
                "Password": 'goodbye',
                "Checking Balance": 2345.30,
                "Savings Balance": 15432.04,
                },

            12345: {
                "Password": 'bye',
                "Checking Balance": 5.65,
                "Savings Balance": 15721.24
                }
            }

    def greetings(self):   # add an if statement to verify the user is here
        print('Hello, Welcome to our bank!')

        self.account_number = input('Please Enter Your Account Number')
        self.password = input('Please Enter Your Password')

        print("Hello, USER NAME HERE")  # need to add the user name variable
        self.welcome = int("what would you like to do today")

    def money_out(self,):

        self.which_account = input('Which account are you transfering money to?')
        self.how_much = int(input('How much are you planing on transfering?'))


def main():
    first_user = BankTeller.greetings('x')

if __name__ == '__main__':
    main()