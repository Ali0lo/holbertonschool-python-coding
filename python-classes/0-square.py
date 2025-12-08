#!/usr/bin/python3

class Square:
    """
    Square class that defines a square by its size.
    
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size  # private attribute

if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))  # Expected output: <class __main__.Square>
    print(mysquare.__dict__)  # Expected output: {_Square__size: 3}

    mysquare = Square(89)
    print(type(mysquare))  # Expected output: <class __main__.Square>
    print(mysquare.__dict__)  # Expected output: {_Square__size: 89}

    try:
        print(mysquare.size)
    except Exception as e:
        print(e)  # Expected output: Square object has no attribute size

    try:
        print(mysquare.__size)
    except Exception as e:
        print(e)  # Expected output: Square object has no attribute __size

