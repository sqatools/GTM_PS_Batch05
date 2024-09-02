class Animal:
    def animal_voice(self):
        pass
    def animal_breed(self):
        pass
    def animal_age(self):
        pass
class Dog(Animal):
    def animal_voice(self):
        print("barking")
    def animal_breed(self):
        print("pamerian")
    def animal_age(self):
        print("the dog is 3yrs old")
obj = Dog()
obj.animal_voice()
#####################################################################
#####################################################################

#Q2:
class Bike:
    def bike_voice(self):
        pass
    def bike_type(self):
        pass
    def bike_average(self):
        pass
class Bullet(Bike):
    def bike_voice(self):
        print("Dugdugdug")
    def bike_type(self):
        print("RoyalEnfield")
    def bike_average(self):
        print("the bike average is 21")
obj = Bullet()
print("_"*50)
obj.bike_voice( )
print("_"*50)
obj.bike_average( )
print("_"*50)
obj.bike_type( )
print("_"*50)