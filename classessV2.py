
class Student:
    uni = "Oxford" # this is a class variable and is shared by everyone
    # functions inside a class are called method
    def get_name(self,s_name, s_age, s_city):
        self.name = s_name # this is called a object variable or a field (acts like a variable)
        self.age  = s_age
        self.city = s_city
        print(self.name)
        print(self.age)
        print(self.city)

john = Student()
john.get_name("John", 43, 'New York')
mike = Student()
mike.get_name("Mike", 23, 'Philly')
Susan = Student()
Susan.get_name("Susan", 55, 'Tampa')
print(Susan.uni)
print(john.uni)









