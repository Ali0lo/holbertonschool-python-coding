#!/usr/bin/python3

class Square:
    """
    Square class that defines a square by its size.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        self.__size = size

if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.__dict__)

    mysquare = Square(89)
    print(type(mysquare))
    print(mysquare.__dict__)

    try:
        print(mysquare.size)
    except Exception as e:
        print(e)

    try:
        print(mysquare.__size)
    except Exception as e:
        print(e)
