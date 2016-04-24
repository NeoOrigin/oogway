#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Csv_Parser
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     14/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

import csv

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Csv_Parser:
    """
    """

    def __init__(self, stream, buffer, delimiter, lineterminator, quotechar, doublequote, escapechar, skipinitialspace ):
        """
        """
        self.stream = stream

        # Because the user may have passed through preferences we register it as another
        # dialect and use that dialect to parse later on
        csv.register_dialect( "custom_1", delimiter        = delimiter,          \
                                          lineterminator   = lineterminator,     \
                                          quotechar        = quotechar,          \
                                          doublequote      = doublequote,        \
                                          escapechar       = escapechar,         \
                                          skipinitialspace = skipinitialspace )

        # Set buffer for unusually large field values
        csv.field_size_limit( buffer )

        self.csvreader = csv.reader( self.stream, dialect = "custom_1" )

    def __iter__(self):
        """
        """
        return self.csvreader

def main():
    pass

if __name__ == '__main__':
    main()