#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Html_Formatter
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

import cgi

from Format.Formatter import Formatter

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Html_Formatter(Formatter):
    """
    Formats any data tables into html tables
    """

    def __init__(self, pretty = True, indent = 3, border_size = 1):
        """
        """
        Formatter.__init__(self)

        self.m_pretty = pretty
        self.m_indent = indent
        self.m_border_size = border_size

    def escape( value ):
        """
        Escapes / converts illegal html characters to ensure data integrity
        """
        return cgi.escape( str( value ) )

    def unescape( value ):
        """
        Unescapes illegal html characters, back to original string
        """
        value = value.replace( "&lt;",   "<" )
        value = value.replace( "&gt;",   ">" )
        value = value.replace( "&quot;", '"' )
        value = value.replace( "&apos;", "'" )

        # this has to be last:
        value = value.replace( "&amp;",  "&" )

        return value

    def write(self, data, out):
        """
        """

        # Write the border if specified
        if self.m_border_size > 0:
            out.write( "<table border=" )
            out.write( self.m_border_size )
            out.write( ">" )
        else:
            out.write( "<table>" )

        if self.m_pretty:
            out.write( "\n" )
            indent1 = " " * self.m_indent
            indent2 = indent1 * 2

            for row_num, row in enumerate( data ):

                outstr = indent1 + "<tr>\n"

                if row_num == 0:
                    for fld in row:
                        outstr += indent2 + "<th>" + escape( fld ) + "</th>\n"
                else:
                    for fld in row:
                        outstr += indent2 + "<td>" + escape( fld ) + "</td>\n"

                out.write( outstr + indent1 + "</tr>\n" )

        else:
            for row_num, row in enumerate( data ):

                outstr = "<tr>"

                if row_num == 0:
                    for fld in row:
                        outstr += "<th>" + escape( fld ) + "</th>"
                else:
                    for fld in row:
                        outstr += "<td>" + escape( fld ) + "</td>"

                out.write( outstr + "</tr>" )
                row_num += 1

        out.write( "</table>" )
        out.flush()

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()