#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Python_Formatter
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

class Python_Formatter(Formatter):
    """
    Formats any data tables into python format
    """

    def __init__(self, pretty = True):
        """
        Constructor for thee Python_Formatter class
        """
        Formatter.__init__(self)

        self.pretty = pretty

    def write(self, data, out):
        """
        """
        if self.pretty:
            out.write( pprint.pformat( data ) )
        else:
            out.write( repr( data ) )

        out.flush()

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()