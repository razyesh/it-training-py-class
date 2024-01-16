# Try and Except
 


a = 12
b = 12

class InvalidInputException(Exception):
    pass

try:
    c = a / b 
    raise InvalidInputException("Input is not valid")
except (TypeError, ZeroDivisionError, NameError, InvalidInputException) as e:
    print(str(e))
    print("Can not concatenate")
else:
    print(c)
finally:
    print("Finanlly executed")


print("After handling exception")