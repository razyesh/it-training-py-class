class Vehicle:
    no_of_wheel = 2 # attributes


class Car(Vehicle):
    no_of_wheel = 4

    def get_wheel(self): # methods
        return self.no_of_wheel

c1 = Car() # object
c1.get_wheel()
print(c1)


