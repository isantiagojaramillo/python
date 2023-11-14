"""System module."""

def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

add(2, 5, 7)
add(2, 5)
add(2, 8, 7, 45, 32)
