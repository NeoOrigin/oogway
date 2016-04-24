#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Field_Value
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Field_Value:
    """
    """

    def __init__(self, raw, actual, format = str, subformat = "", default = None ):
        """
        """
        self.raw        = raw        # The raw string value before formatting
        self.actual     = actual     # The value after formatting
        self.format     = format     # A string detailing the format of the value
        self.subformat  = subformat  # A string detailing extra info for the format
        self.default    = default    # What does the value look like after a default value is replaced in

def main():
    pass

if __name__ == '__main__':
    main()
