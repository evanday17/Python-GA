# don't have a solution to validate they enter numbers yet...maybe could use pypi?

def temp_converter():
    x = (input("What is your temp?"))
    x = float(x)
    y = (x - 32) * 5 / 9
    y = str(round(y,2))

    if x <= 97:
        print("Your temp is pretty low you warm up ASAP")
    elif x >= 100:
        print("Your temp is pretty high, should chill out")
    else:
        print("That is a good looking tempature")

    print("\tIncase you where wondering that is " + y + " in Celsius")

temp_converter()




