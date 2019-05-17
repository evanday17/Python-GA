class Cake:
    # def __int__(self):
    #    print("creating a cupcake") not really sure what this is

    def ingredients(self, i_sugar, i_vin, i_butter, i_salt, i_milk, i_pb):
        self.sugar = i_sugar
        self.vin = i_vin
        self.butter = i_butter
        self.salt = i_salt
        self.milk = i_milk
        self.pb = i_pb
        print("***You will need the following***")
        print(self.sugar, " cups of sugar")
        print(self.vin, " spoons of vin")
        print(self.butter, " ounces of butter")
        print(self.salt, " pinches")
        print(self.milk, " tablespoons of milk")
        print(self.pb, " spoons of pb")


pbbc = Cake()
pbbc.ingredients(4,0,4,6,6,5)


