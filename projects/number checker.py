# check if numbers are odd or even
# this will break if user inputs a str...not what the most efficient way to handle this is

def odd_or_even():
    number = int(input("Pick a number any number!?"))
    if number % 2 == 0:
        print("That is even")
    else:
        print("that is odd")

odd_or_even()


