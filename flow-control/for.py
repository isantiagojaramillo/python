"""System module."""

# for number in range(10):
#     print(number)

# for number in range(10):
#     print(number, number * 'Hello World!')

find = 10
for number in range(10):
    print(number)
    if number == find:
        print("Number found ", find)
        break
else:
    print("I did not find the number")




