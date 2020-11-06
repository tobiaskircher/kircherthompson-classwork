class Dog():
    def __init__(self,my_name,my_colour):
        self.name = my_name
        self.colour = my_colour
    #endprocedure

    def bark(self, bark_times):
        for i in range(bark_times):
            print("Woof!")
        #next i
    #endprocedure
            
#endclass

class Puppy(Dog):
    def __init__(self,my_name,my_colour,my_dob):
        super().__init__(my_name,my_colour)
        self.dob = my_dob
    #endprocedure

    def bark(self,bark_times):
        for i in range(bark_times):
            print("Yap!")
        #next i
    #endprocedure

#endclass

dog1 = Dog("Harry","White")
dog1.bark(3)
puppy1 = Puppy("Larry","Brown","12/08/2020")
puppy1.bark(3)
