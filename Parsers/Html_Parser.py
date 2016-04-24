#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Html_Parser
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     14/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

import sys
import re
import cgi

# Workaround for python 3
try:
    from html.parser import *
except:
    from HTMLParser import *

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

from Format.Html_Formatter   import *

class Html_Parser(HTMLParser):
    """
    """

    def __init__(self, stream, buffer = 8192 ):
        HTMLParser.__init__(self)

        self.data              = []                 # The CSV data
        self.inTD              = False              # Used to track if we are inside or outside a <TD>...</TD> tag.
        self.inTR              = 0                  # Used to track if we are inside or outside a <TR>...</TR> tag.
        self.rowCount          = 0                  # CSV output line counter.
        self.fieldCount        = 0

        self.stream = stream

        # Eventually we'll split this out and parse on demand however for now we do it all up front
        # hoping the input can fit in memory
        raw_data = self.stream.read( buffer )
        while raw_data:
            self.feed( raw_data )
            raw_data = self.stream.read( buffer )

    def handle_starttag(self, tag, attrs):
        """
        Depending on the type of tag that has been started this method sets flags
        to indicate if it is the start of a row or cell definition
        """
        # Note we do not look for a start of <html> or <table> here, this allows us to
        # handle poorly formatted data
        if   tag == 'tr': self.start_tr()
        elif tag == 'td': self.start_td()

    def handle_endtag(self, tag):
        """
        Depending on the type of tag that has been ended this method sets flags
        to indicate if it is the end of a row or cell definition
        """
        if   tag == 'tr': self.end_tr()
        elif tag == 'td': self.end_td()

    def start_tr(self):
        """
        If already within a row the row is closed else we flag that a row is started
        """
        if self.inTR:
            self.end_tr()  # <TR> implies </TR>
        self.inTR = True
        self.fieldCount = 0
        self.data.append( [] )

    def end_tr(self):
        """
        If already within a cell the cell is closed else we flag that a row is started
        """
        if self.inTD:
            self.end_td()  # </TR> implies </TD>

        self.inTR = False
        self.rowCount += 1

    def start_td(self):
        """
        If for some strange reason we are not already in a row we start a row to wrap this cell
        the row's cell contents are wrapped by quotes
        """
        if not self.inTR:
            self.start_tr() # <TD> implies <TR>

        self.inTD   = True
        self.data[ self.rowCount ].append( "" )

    def end_td(self):
        """
        If we are within a cell we end the cell by quoting it, adding a default csv delimiter
        """
        if self.inTD:
            self.inTD = False

        # Get the last cell value for the last row, i.e. the latest
        value = self.data[-1][-1]

        # Now we have completely parsed a cell remove any quote if necessary
        if    ( value.startswith( '"' ) and value.endswith( '"' ) ) \
           or ( value.startswith( "'" ) and value.endswith( "'" ) ):
            value = value[1:-1]

        self.data[-1][-1] = Html_Formatter.unescape( value )
        self.fieldCount   += 1

    def handle_data(self, data):
        """
        Performs limited data cleansing within a cell's value, tabs are replaced with whitespace
        """

        # This parser only handles content within table cells
        if self.inTD:
            self.data[-1][-1] += data

    def handle_entityref(self, data):
        """
        """
        # This parser only handles content within table cells
        if self.inTD:
            self.data[-1][-1] += "&" + data + ";"

    def __iter__(self):
        """
        This object is iterable and returns a copy of itself
        """
        self.index = 0

        return self

    def __next__(self):
        """
        Return the next parsed row (if any)
        """

        # Used to close poorly formed data, i.e. we close arow even if no end of row was found
        if self.inTR:
            self.end_tr()

        # If nothing else to return then stop
        if self.index >= len( self.data ):
            raise StopIteration

        # Else return the data and increment out index for the next use
        data = self.data[ self.index ]
        self.index += 1

        return data

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()