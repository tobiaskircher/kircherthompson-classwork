import inspect
class Dog():
    def __init__(self, myName,myColour):
        self.__name = myName
        self.__colour = myColour
    #end procedure

    def bark(self, barkTimes):
        for i in range(barkTimes):
            print("Woof!")
        #next i
    #end procedure

    def get_colour(self):
        return self.__colour
    #end procedure

    def set_colour(self, newColour):
        self.__colour = newColour
    #end procedure

    def __setattr__(self,attrname,value):
        frame = inspect.currentframe()
        try:
            if "self" in frame.f_back.f_locals: insideclass = True
            else: insideclass = False
        except:
            raise Exception("__getattribute__ function: error in getting frame.f_back.f_locals.")
        finally:
            del frame
        if insideclass == True:
            if attrname == "_Dog__colour":
                if (value.lower() in ['black','brown','white']):
                    self.__dict__[attrname] = value
                else:
                    try:    self.__dict__[attrname]
                    except: self.__dict__[attrname] = ''
                    finally: print("Colour not allowed")
            else:
                self.__dict__[attrname] = value
        else:
            print("Private variable: unable to change value from outside of class")

    #end procedure

    def __getattribute__(self,attr):
        frame = inspect.currentframe()
        try:
            if "self" in frame.f_back.f_locals: insideclass = True
            else: insideclass = False
        except:
            raise Exception("__getattribute__ function: error in getting frame.f_back.f_locals.")
        finally:
            del frame
        if (attr in ["_Dog__name","_Dog__colour"]) and insideclass == False:
            return "Private variable: you can not access the variable's value from outside the class"
        else:
            return super().__getattribute__(attr)

    #end procedure
    
    def get_name(self):
        return self.__name

    #end procedure

#end class

dog1 = Dog("Harry","Black")
print(dog1._Dog__name) #accessing hidden variables
dog1._Dog__name = "Ben"
print(dog1.get_name())
print(dog1.get_colour())
dog1.bark(2)

