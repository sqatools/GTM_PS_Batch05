
class param():
    def __init__(self, dog_breed, dog_name, dog_age): # parameterized constructor
        self.d_breed = dog_breed # instance variable
        self.d_name = dog_name # instance variable
        self.d_age = dog_age # instance variable

        print(f"Dog breed is : {self.d_breed}")
        print(f"Dog name is : {self.d_name}")
        print(f"Dog age is : {self.d_age}")

obj = param("Goldendoodle", "Coco", "9 months") # create object
