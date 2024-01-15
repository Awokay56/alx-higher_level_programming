#!/usr/bin/python3
"""
defines a base model class
"""

class Base:
    """
    Represents the base model
    """

    __nb__objects = 0
    def ___init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

            if __name__ == "__main__":
                b1 = Base( )
                print(b1.id)

                b2 = Base( )
                print(b2.id)

                b3 = Base( )
                print(b3.id)

                b4 = Base(12)
                print(b4.id)

                b5 = Base( )
                print(b5.id)


