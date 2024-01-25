def add(a, b):
    return a + b


def subtract(b, a):
    pass 

def name_of_students(*args, **kwargs):
    pass

# name_of_students(1, 2,3 ,3 ,4,5, 6, 76, a = c, d = e, f= g)

c = add(2, 3)

d = add("abcd", "abc")

e = add([1,2,3], [4,5,6])

f = add(a = 7)
# Student marks : 
"""
{
    1: {"math": 36, "science": 80, "english": 90},
    2: {"math": 36, "science": 80, "english": 90},
    3: {"math": 36, "science": 80, "english": 90},
    4: {"math": 36, "science": 80, "english": 90},
    5: {"math": 36, "science": 80, "english": 90}
}

# create function get_grade(mark) return grade
# https://edusanjal.com/news/letter-grading-system-slc-results/
"""