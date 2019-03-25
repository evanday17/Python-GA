def rates():
    # ask user for deposit and convert to float
    while True:
        try:
            x= (input("how much are you putting down?"))
            x=float(x)
            break
        except:
            print("enter numbers only please")
    # ask user for years and convert to float
    while True:
        try:
            y= (input("how many years will this sit?"))
            y=float(y)
            break
        except:
            print("enter numbers only please")
 
    answer = x * .041 * y
 
    # convert answer to $$$$
    answer = '$' + str(round(answer,2))
 
    print('You will earn ' + answer + " over " + str(y) +  'years')
rates()

