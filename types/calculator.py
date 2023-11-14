"""System module."""

n1 = input("Enter first number: ")
n2 = input("Enter second number: ")

n1 = int(n1)
n2 = int(n2)

add = n1 + n2
subs = n1 - n2
mult = n1 * n2
div = n1 / n2

message = f"""
    For the numbers {n1} and {n2},
    the addition result is: {add},
    the substraction result is: {subs},
    the multiplication result is: {mult},
    the division result is: {div}
"""

print(message)




