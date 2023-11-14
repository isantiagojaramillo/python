"""System module."""

## FUNCTIONS

# def hello():
#     """System module."""

#     print("Hello World!")
#     print("Ultimate Python")


# hello()

## PARAMETERS AND ARGUMENTS

# def hello(name, lastName):
#     """System module."""

#     print("Hello World!")
#     print(f"Welcome {name} {lastName}") #PARAMETERS


# hello("Chanchito", "Happy") # ARGUMENTS

## OPTIONAL ARGUMENTS

# def hello(name, lastName="Happy"):
#     """System module."""

#     print("Hello World!")
#     print(f"Welcome {name} {lastName}")


# hello("Chanchito")

## NAMED ARGUMENTS

def hello(name, lastName="Happy"):
    """System module."""

    print("Hello World!")
    print(f"Welcome {name} {lastName}")


hello(lastName="Happy", name="Chanchito")
