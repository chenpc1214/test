class animal():

    def __init__(self,animal_name,animal_age):
        self.name = animal_name
        self.age = animal_age

    def run(self):
        print(self.name.title(), " is running")

class dog(animal):
    
    def __init__(self, dog_name, dog_age):
        super().__init__("My pet " + dog_name.title(), dog_age)

class bird(animal):
    
    def __init__(self, bird_name, bird_age):
        super().__init__("My pet " +bird_name.title(), bird_age)

    def run(self):
        print(self.name.title(), "is flying")

a = animal("lucy", 5)
print(a.name.title() , " is ", a.age, "years old.")
a.run()

b= dog("lily" , 6)
print(b.name.title(), " is " , b.age, " years old.")
b.run()

c = bird("Cici", 8)
print(c.name.title(), " is ", c.age, " years old.")
c.run()
