# class Vehicle:
#     COLOR = "Red"

#     def __init__(self, color) -> None: # constructor
#         print("called")
#         self.COLOR = color
    
#     def get_color(self):
#         self.COLOR


# truck = Vehicle()

class People:
    NO_OF_HANDS = 2

    def __init__(self, *args, **kwargs): # __repr__ __str__, magic dunder methods
        pass

    def hello():
        pass
    
    def under_16(self):
        self.hello()
        if self.age < 16:
            return True 
        return False 


obj1 = People(age=15)
result = obj1.under_16()
obj1.hello()

print(result)

obj2 = People(age=32)
obj2.under_16()