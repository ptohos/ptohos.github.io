class Dog:                        # The Name of the class starts with a capital
    species = "Terrier"           # Class attributes
    def __init__(self,name,age):  #__init__() the properties of the class.
                                  # It sets the initial state of an object
                                  # typou Dog. It can accept any number of
                                  # parameters but the first is self.
                                  # The rest can be the attributes (data) of
                                  # the object
        self.name = name          # Creation of an attribute called name
                                  # with value name
        self.age  = age           # age with value age. Instance attributes

buddy=Dog("Buddy",9)
jerry=Dog("Jerry",2)
buddy.name                    # Sta attributes den xrisimopoioyntai ()
jerry.age                     # se antithesi me tis methodous
buddy.species
# We can change the atttributes (instance and class)
buddy.age = 10

#We can define two new methods:
class Dog:
    species = "Terrier"
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{sefl.name} says {sound}"


azor = Dog("Azor",4)
azor.description()
azor.speak("Gav Gav")
    

#Anti tis methodou description mporoume na xrisimopoiisoume tin __str__
#Opote i klasi Dog ginetai: 

class Dog:
    species = "Terrier"
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{sefl.name} says {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

#Mporoume na dimiourgisoume mia paragwgi klasi 
class Terrier(Dog):       # put the name of the parent class in ()
    def speak(self, sound="Arf"):
    return f"{self.name} says {sound}"

#Dimiourgia antikeimenou apo tin paragwgi klasi 
miles = Terrier("Miles",4)
miles.speak()            # Den xreiazetai pleon na dwsoume orisma 

# Tha mporousame na exoume prosvasi se sugkekrimeni methodo tis
# mitrikis klassis xrisimopoiontas tin methodo super()
class Terrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound) # It searches for the speak in the parent
    
