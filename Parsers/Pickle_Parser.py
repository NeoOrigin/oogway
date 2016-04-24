#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Pickle_Parser
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     14/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

try:    import cPickle
except: import pickle

class Pickle_Parser:
    """
    """

    def __init__(self, stream, buffer ):
        """
        """
        self.stream = stream

        self.data = pickle.load( stream )

    def __iter__(self):
        """
        """
        self.row_index = 0
        return self

    def __next__(self):
        if self.row_index >= len( self.data ):
            raise StopIteration

        data = self.data[ self.row_index ]

        self.row_index += 1

        return data

def main():
    pass

if __name__ == '__main__':
    main()
