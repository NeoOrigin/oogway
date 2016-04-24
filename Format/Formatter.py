#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Formatter
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

class Formatter:
    """
    The base class for all Formatter objects
    """

    def __init__(self):
        """
        """
        pass

    def get_max_width(data, field_index):
        """
        Get the maximum width of the given column index
        """

        return max( [ len( str( row[ field_index ] ) ) for row in data ] )

    def get_min_width(data, field_index):
        """
        Get the minimum width of the given column index
        """

        return min( [ len( str( row[ field_index ] ) ) for row in data ] )

    def get_avg_width(data, field_index):
        """
        Get the average width of the given column index
        """

        return float( sum( [ len( str( row[ field_index ] ) ) for row in data ] ) ) / len( data )

    def write( self, data, out ):
        """
        """
        pass

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()