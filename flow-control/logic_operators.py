"""System module."""

# AND, OR, NOT

gas = False
turnOn = True
age = 18

# if gas and turnOn:
#     print("You can move forward")

# if gas or turnOn:
#     print("You can move forward")

if not gas and (turnOn or age > 17):
    print("You can move forward")



