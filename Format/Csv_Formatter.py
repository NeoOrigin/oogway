#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Csv_Formatter
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

import csv

from Format.Formatter import Formatter

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Csv_Formatter(Formatter):
    """
    Formats any data tables into CSV format
    """

    def __init__(self, delimiter = "|", escapechar="\\", quotechar='"', skipinitialspace=True, lineterminator="\n", doublequote=False):
        """
        Constructor for the Csv_Formatter class
        """
        Formatter.__init__(self)

        self.delimiter        = delimiter
        self.escapechar       = escapechar
        self.quotechar        = quotechar
        self.skipinitialspace = skipinitialspace
        self.lineterminator   = lineterminator
        self.doublequote      = doublequote

    def write(self, data, out):
        """
        """
        writer = csv.writer( out, delimiter        = self.delimiter,        \
                                  escapechar       = self.escapechar,       \
                                  quotechar        = self.quotechar,        \
                                  skipinitialspace = self.skipinitialspace, \
                                  lineterminator   = self.lineterminator,   \
                                  doublequote      = self.doublequote )
        writer.writerows( data )

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()