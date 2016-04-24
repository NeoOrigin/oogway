#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Tracker
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

from Profiles.Counter import *

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Tracker:
    """
    A basic value tracker used as the basis for most metrics
    """

    def __init__(self):
        """
        Constructor for the Tracker class
        """
        self.m_data = {};

    def count(self):
        """
        Returns the number of items being tracked
        """
        return len( self.m_data )

    def get_tracked_keys(self):
        """
        Returns the keys being tracked
        """
        return self.m_data.keys()

    def track(self, key):
        """
        """
        c = self.m_data.get( key )
        if c == None:
            c = Counter(1)
        else:
            c.increment()

        self.m_data[ key ] = c

    def clear(self):
        """
        """
        self.m_data = {}

    def remove(self, key):
        """
        """
        del self.m_data[ key ]

    def reset(self, key):
        """
        """
        self.m_data[ key ] = Counter()

    #def increment(self, key):
    #    """
    #    """
    #    self.m_data[ key ] = self.m_data.get( key, 0 ) + 1

    def has_value(self, key):
        """
        """
        return key in self.m_data

    def get_value(self, key):
        """
        """
        return self.m_data[ key ]

    def set_value(self, key, value):
        """
        """
        v = value
        if not isinstance( v, Counter ):
            v = Counter( value )

        self.m_data[ key ] = v

    def __str__(self):
        """
        """
        return str( self.m_data )

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()