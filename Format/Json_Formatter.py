#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Json_Formatter
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

import json

from Format.Formatter import Formatter

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Json_Formatter(Formatter):
    """
    Formats data tables into Json objects
    """

    def __init__(self, pretty = True ):
        """
        """
        Formatter.__init__(self)

        self.m_pretty = pretty

    def write(self, data, out):
        """
        """
        if self.m_pretty:
            json.dump( data, out, sort_keys=True, indent=4)
        else:
            json.dump( data, out )

        out.flush()

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()