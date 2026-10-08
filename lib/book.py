#!/usr/bin/env python3
# Represents a book with a title and a page count
class Book:

    def __init__(self, title, page_count):

        self.title = title

        self.page_count = page_count



    @property

    def page_count(self):

        return self._page_count



    @page_count.setter

    def page_count(self, value):

        if isinstance(value, int):

            self._page_count = value

        else:

            print("page_count must be an integer")


# Prints a message when a page is turned
    def turn_page(self):

        print("Flipping the page...wow, you read fast!")


    
        