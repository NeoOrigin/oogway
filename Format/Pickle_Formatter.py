#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Pickle_Formatter
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

from Format.Formatter import Formatter

import pprint

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

try:    import cPickle
except: import pickle

class Pickle_Formatter(Formatter):
    """
    Formats any data tables into python pickle format
    """

    def __init__(self, pretty = True):
        """
        Constructor for thee Pickle_Formatter class
        """
        Formatter.__init__(self)

        self.pretty = pretty

    def write(self, data, out):
        """
        """
        pickle.dump( data, out )

        out.flush()

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()