#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Table_Formatter
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

class Table_Formatter(Formatter):
    """
    Formats any data tables into a basic table format
    """

    def __init__(self, lines = True, header = 1, alignment = None ):
        """
        Constructor for the Table_Formatter class
        """
        Formatter.__init__(self)

        self.m_display_lines = lines
        self.m_header        = header
        self.m_alignment     = None

    def set_alignment( self, alignment ):
        """
        """
        self.m_alignment = alignment

    def write(self, data, out):
        """
        """
        col_paddings = []

        # Finds the largest field value size for each field
        for i in range( len( data[ 0 ] ) ):
            col_paddings.append( Formatter.get_max_width( data, i ) )

        # Build a horizontal border line
        h_line     = "+"
        for bounds in col_paddings:
            h_line += "-" * ( bounds + 2 ) + "+"

        h_line += "\n"
        out.write( h_line )

        # Setup for csv output
        writer = csv.writer( out, delimiter = "|", escapechar = "\\" )

        # Find out the size of the alignments
        num_alignments = -1
        if self.m_alignment != None:
            num_alignments = len( self.m_alignment )

        # Now go through our data to print out
        for row_number, row in enumerate( data ):

            if self.m_header > 0 and self.m_header == row_number:
                out.write( h_line )

            new_row = [ "" ]

            # rest of the cols
            for i in range( 0, len( row ) ):
                val     = str( row[i] )
                padding = col_paddings[i] + 2

                # Use default alignment if none specified or we dont have enough
                if self.m_alignment == None or i > num_alignments:
                    val = val.rjust( padding )
                else:
                    if self.m_alignment == "left":
                        val = val.ljust( padding )
                    elif self.m_alignment == "right":
                        val = val.rjust( padding )
                    else:
                        val = val.center( padding )

                new_row.append( val )

            new_row.append( "" )
            writer.writerow( new_row )

        out.write( h_line )
        out.flush()

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()