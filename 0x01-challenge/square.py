#!/usr/bin/python3
"""
Class Square Module
"""

class Square():
    
    def __init__(self, width=0, height=0):
        # Initialize the width and height of the square
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ 
        Calculates the area of the square
        
        Returns:
        int: The area of the square
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ 
        Calculates the perimeter of the square
        
        Returns:
        int: The perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        # Return a string representation of the square
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    # Create a square object with width=12 and height=9
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
