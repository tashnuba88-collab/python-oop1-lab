#!/usr/bin/env python3
# Represents a coffee with a size and a price
class Coffee:

    def __init__(self, size, price):

        self.size = size

        self.price = price



    @property

    def size(self):

        return self._size



    @size.setter

    def size(self, value):

        if value in ("Small", "Medium", "Large"):

            self._size = value

        else:

            print("size must be Small, Medium, or Large")


# Prints a thank-you message and raises the price by 1
    def tip(self):

        print("This coffee is great, here’s a tip!")

        self.price += 1



