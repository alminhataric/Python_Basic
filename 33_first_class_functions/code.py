""" def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result) """


##############################################################################################################################

from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
        raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wol", "age": 30},
    {"name": "Anne Pun", "age": 27}
]



print(search(friends, "Rolf Smith", itemgetter("name")))