#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Max_Values_Metric
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

class Max_Values_Metric(Metric.Metric):
    """
    Tracks the highest values encountered
    """

    def __init__(self, field_profile, limit = 10):
        """
        Constructor for the Max_Values_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.values = []
        self.limit = limit

    def analyse(self, field_value):
        """
        """
        if field_value .actual not in self.values:
            # sort our value into our sliding window
            bisect.insort( self.values, field_value.actual )

            # If our window is so big then resize it
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
