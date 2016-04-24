#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        profiler
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Counter:
    """
    A basic counter used as the basis for most metrics
    """

    def __init__(self, count = 0):
        """
        Constructor for the Counter class
        """
        self.m_count = count;

    def get_count(self):
        """
        Returns the current count calculated by this Counter
        """
        return self.m_count

    def set_count(self, count):
        """
        Sets the current count for this Counter
        """
        self.m_count = count

    def add(self, amount):
        """
        Adds a specified amount to this Counter
        """
        self.m_count += amount

    def deduct(self, amount):
        """
        """
        self.m_count -= amount

    def increment(self):
        """
        """
        self.m_count += 1

    def decrement(self):
        """
        """
        self.m_count -= 1

    def get_average(self, total, rounding = None):
        """
        """
        t = total
        if isinstance(total, Counter):
            t = total.get_count()

        value = float( self.m_count ) / t

        if rounding != None:
            value = round( value, rounding )
        return value

    def get_percentage(self, total, rounding = None ):
        """
        """
        return self.get_average( total, rounding ) * 100

    def __lt__(self, right):
        """
        """
        return self.m_count < right

    def __gt__(self, right):
        """
        """
        return self.m_count > right

    def __le__(self, right):
        """
        """
        return self.m_count <= right

    def __ge__(self, right):
        """
        """
        return self.m_count >= right

    def __eq__(self, right):
        """
        """
        return self.m_count == right

    def __ne__(self, right):
        """
        """
        return self.m_count != right

    def __str__(self):
        """
        """
        return str( self.m_count )

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()