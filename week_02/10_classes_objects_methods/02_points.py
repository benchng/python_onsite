'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


