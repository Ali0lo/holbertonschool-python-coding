#!/usr/bin/python3

class Square:
    """
    Class that defines a square by its size.
    
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
    # Test case 1: Create an instance of Square with size 3
    mysquare = Square(3)
    print(type(mysquare))  # Expected output: <class '__main__.Square'>
    print(mysquare.__dict__)  # Expected output: {'_Square__size': 3}

    # Test case 2: Create an instance of Square with size 89
    mysquare = Square(89)
    print(type(mysquare))  # Expected output: <class '__main__.Square'>
    print(mysquare.__dict__)  # Expected output: {'_Square__size': 89}

    # Test case 3: Accessing size directly should raise an error
    try:
        print(mysquare.size)
    except Exception as e:
        print(e)  # Expected output: 'Square' object has no attribute 'size'

    # Test case 4: Trying to access the private attribute __size directly
    try:
        print(mysquare.__size)
    except Exception as e:
        print(e)  # Expected output: 'Square' object has no attribute '__size'
