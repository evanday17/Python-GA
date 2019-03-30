
def compute_rec():
    z = (input('What type of units are you using? Cms? Ft? ect'))  # could spend more time refining this part
    print("PLEASE ENTER ONLY NUMBERS TO THE FOLLOWING QUESTIONS")

    while True:  # loops so we require ints instead of strs...this is a better way to do this just not sure of how yet

        try:
            x = (input("how tall is the rectangle?"))
            x = float(x)  # checks if answer is number
            break  # need to break or it loops forever...probably isn't the best way to do this
        except:
            print("enter numbers only please")
    while True:

        try:
            y = (input("how long is the rectangle?"))
            y = float(y)
            break
        except:
            print("enter numbers only please")

    area = x * y
    area = str(round(area, 2)) #rounds float 2 decimal places
    print("Got it, the area of your rectangle is " + area + " " + z +)

compute_rec()
