"""System module."""

## A METHOD IS A FUNCTION THAT IS INSIDE AN OBJECT.

animal = " Happy Chanchito "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal.strip()) ## DELETES THE SPACES
print(animal.strip().capitalize())
print(animal.lstrip()) ## DELETES THE SPACES IN THE LEFT
print(animal.rstrip()) ## DELETES THE SPACES IN THE RIGTH
print(animal.find("ch"))
print(animal.find("kt")) ##RETURNS THE INDEX
print(animal.replace("nch", "pepito"))
print("nch" in animal)
print("jiji" in animal) ## RETURNS THE Boolean






