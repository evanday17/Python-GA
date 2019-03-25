
def compute_rec():

    while True:  # loops so we require ints instead of strs

        print("PLEASE ENTER ONLY NUMBERS TO THE FOLLOWING QUESTIONS")

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
        print(area)

    '''print(area)
            area = str(round(area, 2))
            print("Got it, the area of your rectangle is " + area)'''


compute_rec()
