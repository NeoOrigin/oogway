#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Max_Length_Values_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import Metric
import Profiles.Tracker

import bisect

class Max_Length_Values_Metric(Metric.Metric):
    """
    Counts null values encountered
    """

    def __init__(self, field_profile, limit = 10):
        """
        Constructor for the Max_Length_Values_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.values = []
        self.limit = limit

    def analyse(self, field_value):
        """
        """

        # Get the length of the value and determine where its position would be
        # in our sliding window if we were to add it
        l   = len( str( field_value.actual ) )
        pos = bisect.bisect( self.values, l )

        if pos > 0:
            self.values.insert( pos, field_value.actual )

        if len( self.values ) > self.limit:
            self.values = self.values[1:]

    def get_result(self):
        """
        """
        return self.values


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
