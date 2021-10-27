""" def add(x, y):
    result = x + y
    print(result)

add(5, 3) """


################################################################################################################


""" def say_hello(name, surename):
    print(f"Hello!, {name} {surename}" )

say_hello(surename="Bob", name="Smith") """


################################################################################################################


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend /divisor)
    else:
        print("You fool!")

divide(dividend=15,divisor=0)

