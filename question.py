""" 
Write a function that uses list comprehension 
to generate a 
list of squares of the numbers from 1 to n.
"""

# n = input("Please enter the number") # user sanga number mageko 

def generate_square(number):
    """
    returns square of number
    """
    return number**2


def generate_square_of_list_of_numbers(*args): 
    """
    *args -> number of argument to accept

    """
    # print(args)
    # for arg in args:
    #     print(arg)
    #     print(generate_square(arg))
    return [generate_square(arg) for arg in args]


# list_of_numbers = range(1, n+1)

# # generate_square_of_list_of_numbers(1, 2, 3, 4, 5,6,7)

# results=generate_square_of_list_of_numbers(*list_of_numbers)

# input = [[ 1, 2, 3],
#   [4, 5, 6]]

# [[1,4],[2,5],[3,6]]

# new_list = []
# for i in input:
#     new_list2 = []
#     for a in i:
#         pass


generate_square(1)
generate_square(2)
generate_square(5)


# add = lambda x, y: x + y


